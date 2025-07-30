"""
Configuration settings for the thermal swelling simulation.

Author: Sosuke Ichihashi
Date: 2025-07-29
"""

from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class Config:
    # Ambient temperature in degrees Celsius
    ambient_temperature: float = 20.0  # °C

    # Target temperature for the swelling process in degrees Celsius
    swell_temperature: float = 145.0  # °C

    # Power of the light source used for heating in watts
    light_power: float = 100.0        # W

    # Diameter of the light beam in meters
    light_diameter: float = 0.06      # m

    # Thermal diffusivity of the material in m^2/s
    alpha: float = 5e-7               # m²/s

    # Density of the paper in kg/m² (assumes 0.1 mm thickness)
    density_paper: float = 0.08       # kg/m²

    # Specific heat capacity of paper in J/kg·K
    c_paper: float = 1340.0           # J/kg·K

    # Absorption coefficient of paper (fraction of incident energy absorbed)
    absorb_paper: float = 0.96

    # Stefan–Boltzmann constant in W/m²·K⁴
    sigma: float = 5.67e-8            # W/m²·K⁴

    # Convective heat transfer coefficient in W/m²·K
    h: float = 9.00                   # W/m²·K

    # Upper threshold for image or signal processing
    upper_threshold: int = 256

    # Lower threshold for image or signal processing
    lower_threshold: int = 20

    # Buffer margin used in calculations (unitless or context-specific)
    buffer: float = 10.0

    # Duration for which heating is applied, in seconds
    heating_time: float = 6.0        # s

    # Maximum number of iterations for an algorithm or loop
    max_iterations: int = 300

    # Enabling logging
    verbose: int = 1

    # Number of cells the paper is divided into in thermal simulations
    resolution: int = 120000         # px²

    @staticmethod
    def from_file(path: Path) -> "Config":
        """
        Load configuration parameters from a JSON file.
        Only a subset of parameters are loaded; others use default values.
        """
        with open(path, 'r') as f:
            data = json.load(f)

        return Config(
            swell_temperature=data.get('swell_temperature', 145.0),
            light_power=data.get('light_power', 100.0),
            light_diameter=data.get('light_diameter', 0.06),
            alpha=data.get('alpha', 1e-7),
            verbose=data.get('verbose', 1),
            resolution=data.get('resolution', 120000)
        )
