# MIT License
# Copyright (c) 2025 Sosuke Ichihashi
# 
# This file is part of the Swell by Light research software.
# See: https://dl.acm.org/doi/10.1145/3689050.3704420
# Project page: https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.


"""
Utility functions for image processing and heatmap scaling.

Author: Sosuke Ichihashi
Date: 2025-07-29
"""

from PIL import Image
from typing import Tuple
import numpy as np

def compute_dims(img: Image.Image) -> Tuple[float, float]:
    """
    Compute the physical dimensions of an image based on its DPI.

    Args:
        img: A PIL Image object.

    Returns:
        A tuple containing:
            - Image width in pixels
            - Image height in pixels
            - Image width in meters
            - Image height in meters
    """
    dpi_x, dpi_y = img.info.get('dpi', (72, 72))  # Default to 72 DPI if not provided
    phys_w = img.width * 0.0254 / dpi_x           # Convert width from pixels to meters
    phys_h = img.height * 0.0254 / dpi_y          # Convert height from pixels to meters
    return img.width, img.height, phys_w, phys_h

def scale_to_255(H, max_heat: float):
    """
    Scale a heatmap array to the 0–255 range for visualization.

    Args:
        H: A NumPy array of heat values.
        max_heat: The maximum expected heat value used for normalization.

    Returns:
        A NumPy array of type uint8 scaled to the 0–255 range.
    """
    scaled = H * 255 / max_heat                   # Normalize to 0–255 range
    return np.clip(scaled, 0, 255).astype(np.uint8)  # Clip values and convert to uint8
