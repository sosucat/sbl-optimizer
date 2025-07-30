"""
I/O utilities for saving simulation outputs such as patterns, error logs, and temperature plots.

Author: Sosuke Ichihashi
Date: 2025-07-29
"""

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from pathlib import Path
from .utils import scale_to_255


def save_pattern(img_path: Path, H, max_heat):
    """
    Generate and save a PDF pattern image from a heatmap.

    Args:
        img_path: Path to the input image used for sizing and DPI.
        H: Heatmap array (2D).
        max_heat: Maximum heat value used for scaling.

    Returns:
        Path to the saved PDF file.
    """
    img = Image.open(img_path)
    
    # Convert heatmap to 8-bit grayscale image and invert it
    pattern = ImageOps.invert(Image.fromarray(scale_to_255(H, max_heat)))
    
    # Resize pattern to match original image dimensions
    pattern = pattern.resize(img.size, resample=Image.Resampling.BILINEAR)
    
    # Create output file path
    out = Path.cwd() / f"{img_path.stem}_opt.pdf"
    
    # Save pattern with original DPI
    pattern.save(out, dpi=img.info.get('dpi', (72, 72)))
    return out


def save_errors(errors, path: Path = Path('errors.csv')):
    """
    Save a list of integer errors to a CSV file.

    Args:
        errors: List or array of error values.
        path: Destination file path for saving (default: 'errors.csv').

    Returns:
        Path to the saved CSV file.
    """
    full_path = Path.cwd() / path
    np.savetxt(full_path, np.array(errors, dtype=int), delimiter=',', fmt='%d')
    return full_path


def save_plots(T, phys_w, phys_h, img_path: Path, dpi: int):
    """
    Generate and save contour plots from temperature data.

    Args:
        T: 2D NumPy array of temperature values.
        phys_w: Physical width of the object in meters.
        phys_h: Physical height of the object in meters.
        img_path: Path to the reference image (for naming and sizing).
        dpi: Desired DPI for output plots.

    Returns:
        List of paths to the saved plot images.
    """
    # Open image to retrieve pixel dimensions
    img = Image.open(img_path)
    dpi_x = dpi
    dpi_y = dpi

    # Convert image size from pixels to inches
    width_in = img.width / dpi_x
    height_in = img.height / dpi_y

    # Create meshgrid in physical space (meters)
    X, Y = np.meshgrid(
        np.linspace(0, phys_h, T.shape[1]),
        np.linspace(0, phys_w, T.shape[0])
    )

    # Define contour levels and suffixes for output files
    levels_list = [
        ([0, 140, 180, 300], '_swell.png'),
        ([0, 20, 40, 60, 80, 100, 120, 140, 160], '_temperature.png')
    ]

    outs = []
    for levels, suf in levels_list:
        # Set up figure with padding to avoid clipping
        plt.figure(figsize=(width_in + 1.5, height_in), dpi=dpi_x)
        plt.contourf(X, Y[::-1], T, levels)
        cb = plt.colorbar()
        cb.ax.tick_params(labelsize=20)
        plt.xticks([])
        plt.yticks([])

        # Save the plot image
        out = Path.cwd() / f"{img_path.stem}{suf}"
        plt.savefig(out)
        plt.close()
        outs.append(out)

    return outs
