"""
Heat solver for simulating temperature distribution and adaptive heat pattern optimization.

Author: Sosuke Ichihashi
Date: 2025-07-29
"""

import math
import logging
import numpy as np
from PIL import Image
from .utils import compute_dims
from .config import Config


logger = logging.getLogger(__name__)

def configure_logger(verbose: bool):
    """
    Configure logger based on verbosity setting.
    """
    if verbose:
        logger.setLevel(logging.INFO)
        logger.propagate = False  # Prevent messages from going to the root logger
        if not logger.handlers:
            ch = logging.StreamHandler()
            ch.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
            logger.addHandler(ch)
    else:
        logger.setLevel(logging.WARNING)


def image_to_heat_pattern(image_path, config: Config):
    """
    Convert an input image into a binary mask and an initial heatmap.

    Args:
        image_path: Path to the image.
        config: Config object containing simulation parameters.

    Returns:
        Tuple containing:
            - mask: Binary array indicating active heating region.
            - H_init: Initial heatmap based on mask.
            - max_heat: Maximum heat that can be applied per cell.
    """
    img = Image.open(image_path)

    # Rescale image to match the resolution of thermal simulations
    scale = math.sqrt(config.resolution / (img.width * img.height))
    img_rs = img.resize(
        (int(img.width * scale), int(img.height * scale)),
        resample=Image.Resampling.LANCZOS
    )

    # Convert to grayscale and threshold
    gray = img_rs.convert('L')
    arr = 255 - np.array(gray)
    mask = (arr < config.upper_threshold) & (arr >= config.lower_threshold)

    # Compute physical dimensions and grid spacing
    _, _, phys_w, phys_h = compute_dims(img)
    nx, ny = mask.shape
    dx = phys_w / (nx - 1)
    dy = phys_h / (ny - 1)

    # Compute timestep
    dt = 0.49 * dx**2 * dy**2 / ((dx**2 + dy**2) * config.alpha)

    # Estimate maximum heat per cell
    area_cell = phys_w * phys_h / (nx * ny)
    total_area = config.light_diameter**2 * math.pi / 4
    actual_light_power = config.light_power * 0.4
    max_heat = (actual_light_power / total_area) * area_cell * dt * config.absorb_paper
    default_heat = max_heat / 2

    return mask, mask.astype(float) * default_heat, max_heat


def apply_heat_losses(Q_rad: np.ndarray,
                      Q_conv: np.ndarray,
                      T: np.ndarray,
                      H: np.ndarray,
                      max_heat: float,
                      dx: float,
                      dy: float,
                      dt: float,
                      config: Config):
    """
    Compute radiative and convective heat losses for each grid cell.

    Fills Q_rad and Q_conv arrays in-place.

    Args:
        Q_rad: Output array for radiative losses [J].
        Q_conv: Output array for convective losses [J].
        T: Temperature field in °C.
        H: Heatmap array for emissivity calculation.
        max_heat: Maximum applied heat per cell.
        dx, dy: Spatial resolution in meters.
        dt: Timestep in seconds.
        config: Simulation configuration.
    """
    A = dx * dy  # Area per cell in m²

    # Convert temperatures to Kelvin
    T_abs = T + 273.15
    T_amb = config.ambient_temperature + 273.15

    # Emissivity estimation (clamped by H)
    E = 0.68 + 0.22 * H / max_heat

    # Radiative loss
    Q_rad[:] = config.sigma * E * (T_abs**4 - T_amb**4) * A * dt

    # Convective loss
    Q_conv[:] = config.h * (T - config.ambient_temperature) * A * dt


def add_heat(T: np.ndarray, H: np.ndarray, Q_rad: np.ndarray,
             Q_conv: np.ndarray, phys_w: float, phys_h: float,
             config: Config):
    """
    Update the temperature field T by adding net heat input.

    Args:
        T: Temperature field in °C (updated in-place).
        H: Heat input array.
        Q_rad: Radiative losses.
        Q_conv: Convective losses.
        phys_w, phys_h: Physical dimensions in meters.
        config: Simulation configuration.
    """
    # Heat capacity per cell
    hc_paper = config.c_paper * config.density_paper * phys_w * phys_h / (T.shape[0] * T.shape[1])
    T += (H - (Q_rad + Q_conv) * 2) / hc_paper


def update_heat_pattern(T: np.ndarray, H: np.ndarray, mask: np.ndarray,
                        swell_temperature: float, buffer: float,
                        max_heat_rate: float):
    """
    Adjust heat pattern based on local temperature and region mask.

    Args:
        T: Temperature field.
        H: Heat input field (updated in-place).
        mask: Boolean array indicating regions of interest.
        swell_temperature: Target temperature.
        buffer: Tolerance above target temperature.
        max_heat_rate: Maximum allowable heat per cell.
    """
    nx, ny = T.shape
    for i in range(nx):
        for j in range(ny):
            if mask[i, j]:
                if T[i, j] > swell_temperature + buffer:
                    radius = math.e - 1
                    rate_factor = max_heat_rate / 256 * 2
                elif T[i, j] < swell_temperature:
                    H[i, j] = min(max_heat_rate, H[i, j] + max_heat_rate / 256)
                    continue
                else:
                    continue
            else:
                if T[i, j] > swell_temperature:
                    radius = 2 * math.e
                    rate_factor = max_heat_rate / 256 / 21.5
                else:
                    continue

            r_int = math.floor(-radius)
            r_ceil = math.ceil(radius)
            for di in range(r_int, r_ceil + 1):
                ii = i + di
                if not (0 <= ii < nx):
                    continue
                for dj in range(r_int, r_ceil + 1):
                    jj = j + dj
                    if not (0 <= jj < ny):
                        continue
                    dist_sq = di * di + dj * dj
                    if 0 < dist_sq < radius * radius:
                        dist = math.sqrt(dist_sq)
                        dec = rate_factor * math.log((math.e if mask[i, j] else 2 * math.e) / dist)
                        H[ii, jj] = min(max_heat_rate, max(0.0, H[ii, jj] - dec))


def count_outsiders(T: np.ndarray, mask: np.ndarray, config: Config) -> int:
    """
    Count the number of grid points that violate thermal constraints.

    Args:
        T: Temperature field.
        mask: Region of interest.
        config: Simulation configuration.

    Returns:
        Number of error points (outside acceptable temperature range).
    """
    errs = 0
    for t, m in zip(T.flat, mask.flat):
        if m:
            if t < config.swell_temperature or t > config.swell_temperature + config.buffer:
                errs += 1
        else:
            if t > config.swell_temperature + config.buffer:
                errs += 1
    return errs


def is_converged(errors: list[int]) -> bool:
    """
    Check if the optimization process has converged.

    Args:
        errors: List of error counts per iteration.

    Returns:
        True if errors have plateaued in recent iterations, else False.
    """
    if len(errors) < 20:
        return False
    return min(errors[-20:-10]) < min(errors[-10:])


def optimize(mask, H_init, max_heat, img_w, img_h, phys_w, phys_h, config: Config):
    """
    Perform iterative optimization to generate an adaptive heatmap.

    Args:
        mask: Binary mask indicating swelling region.
        H_init: Initial heat input.
        max_heat: Maximum heat value.
        img_w, img_h: Image dimensions in pixels (unused).
        phys_w, phys_h: Physical dimensions in meters.
        config: Configuration parameters.

    Returns:
        Tuple of:
            - T_best: Best temperature field achieved.
            - H: Final heat input field.
            - errors: List of error counts over iterations.
    """
    configure_logger(config.verbose == 1)

    dx = phys_w / (mask.shape[0] - 1)
    dy = phys_h / (mask.shape[1] - 1)
    dt = 0.49 * dx**2 * dy**2 / ((dx**2 + dy**2) * config.alpha)
    nt = int(config.heating_time / dt)

    errors = []
    T_best = np.ones_like(H_init) * config.ambient_temperature
    H = H_init.copy()
    Q_rad = H_init.copy()
    Q_conv = H_init.copy()

    for it in range(config.max_iterations):
        # Update heat pattern after first iteration
        if it > 0:
            update_heat_pattern(
                T, H, mask,
                config.swell_temperature, config.buffer,
                max_heat
            )

        # Reset temperature field to ambient
        T = np.ones_like(H) * config.ambient_temperature

        # Time-stepping for heat diffusion
        for _ in range(nt):
            Tn = T.copy()
            T[1:-1, 1:-1] = (
                Tn[1:-1, 1:-1]
                + (config.alpha * dt / dx**2) * (Tn[1:-1, 2:] - 2 * Tn[1:-1, 1:-1] + Tn[1:-1, :-2])
                + (config.alpha * dt / dy**2) * (Tn[2:, 1:-1] - 2 * Tn[1:-1, 1:-1] + Tn[:-2, 1:-1])
            )
            apply_heat_losses(Q_rad, Q_conv, T, H, max_heat, dx, dy, dt, config)
            add_heat(T, H, Q_rad, Q_conv, phys_w, phys_h, config)

        # Track and store error
        err = count_outsiders(T, mask, config)
        errors.append(err)

        # Log the iteration number and the error count
        logger.info(f"Iteration {it + 1}: Outlier = {int(err * 100 / config.resolution)}%")

        # Store best temperature result
        if err < min(errors[:-1] or [err]):
            T_best = T.copy()

        if is_converged(errors):
            logger.info(f"Converged at iteration {it + 1}.")
            break

    return T_best, H, errors
