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
Main entry point for running the heat optimization process.

Author: Sosuke Ichihashi
Date: 2025-07-29
"""

import argparse
import logging
from pathlib import Path
from PIL import Image
import importlib.resources as resources

from .config import Config
from .heat_solver import image_to_heat_pattern, optimize
from .utils import compute_dims
from .io import save_pattern, save_errors, save_plots


def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace containing input image path and config path.
    """
    # Use importlib.resources to get path to config.json bundled in the package
    try:
        with resources.as_file(resources.files("sbl_optimizer") / "config.json") as config_path:
            default_cfg = str(config_path)
    except (FileNotFoundError, ModuleNotFoundError):
        default_cfg = "config.json"  # Fallback

    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Input image path')
    parser.add_argument(
        '-c', '--config',
        default=str(default_cfg),
        help=f'Path to JSON config (default: {default_cfg})'
    )
    return parser.parse_args()


def main():
    """
    Main execution function:
    - Loads configuration and input image.
    - Generates initial heat pattern.
    - Optimizes heat distribution.
    - Saves output pattern, error log, and temperature plots.
    """
    args = parse_args()

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

    # Load config and image
    cfg = Config.from_file(Path(args.config))
    image_path = Path(args.image)
    mask, H_init, max_heat = image_to_heat_pattern(image_path, cfg)

    # Get physical dimensions
    img_w, img_h, phys_w, phys_h = compute_dims(Image.open(image_path))

    # Run optimization
    T_best, H_best, errors = optimize(mask, H_init, max_heat, img_w, img_h, phys_w, phys_h, cfg)

    # Save results
    out_pdf = save_pattern(image_path, H_best, max_heat)
    # Comment out the line below to track error scores
    # err_csv = save_errors(errors)
    plots = save_plots(T_best, phys_w, phys_h, image_path, dpi=Image.open(image_path).info.get('dpi', (72, 72))[0])

    # Log output file paths
    logging.info("Saved pattern: %s", out_pdf)
    # Comment out the line below to save the tracked error scores. You need to comment out the tracking line above.
    # logging.info("Saved errors: %s", err_csv)
    for p in plots:
        logging.info("Saved plot: %s", p)


if __name__ == '__main__':
    main()
