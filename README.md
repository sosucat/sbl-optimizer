# sbl-optimizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![PyPI version](https://badge.fury.io/py/sbl-optimizer.svg)](https://badge.fury.io/py/sbl-optimizer)\
 [Homepage](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/) • [Paper](https://doi.org/10.1145/3689050.3704420) • [PyPI](https://pypi.org/project/sbl-optimizer/) • [GitHub](https://github.com/sosucat/sbl-optimizer)

Thermal swell pattern optimizer for “Swell by Light”: an approachable technique for freeform raised textures on paper and other materials.  
Generates improved print patterns that considers heat diffusion, resulting in swell patterns similar to those of the original image.

---

## Table of Contents

- [sbl-optimizer](#sbl-optimizer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Using a Virtual Environment (Optional)](#using-a-virtual-environment-optional)
    - [Install **sbl-optimizer** in two easy ways:](#install-sbl-optimizer-in-two-easy-ways)
      - [1. From PyPI](#1-from-pypi)
      - [2. From Source](#2-from-source)
    - [Requirements](#requirements)
  - [Quick Start](#quick-start)
  - [Configuration](#configuration)
  - [Command Line Interface](#command-line-interface)
    - [Usage](#usage)
    - [Arguments](#arguments)
    - [Options](#options)
  - [Examples](#examples)
  - [Citation](#citation)
  - [Contributing](#contributing)
  - [License](#license)

---

## Features

- **Adaptive heat‐pattern optimization**  
  Compensates for heat diffusion to produce raised textures that match your design.
- **Simple CLI**  
  One‐command execution, with JSON‐based configuration and image input.
- **Built on Python**  
  Uses NumPy, Pillow, and Matplotlib for fast, portable computations and visualizations.

---

## Installation

We recommend using a virtual environment to manage dependencies cleanly and avoid conflicts:

### Using a Virtual Environment (Optional)

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# Then install the package
pip install sbl-optimizer
```

### Install **sbl-optimizer** in two easy ways:


#### 1. From PyPI

The simplest method—just pip:

```bash
pip install sbl-optimizer
```

#### 2. From Source

Clone the repository and install locally:

```bash
git clone https://github.com/sosucat/sbl-optimizer.git
cd sbl-optimizer
pip install .
```

### Requirements

Ensure you have Python and dependencies:
| Libraries  | Versions   |
| ---------- | ---------- |
| Python     | 3.9 – 3.11 |
| NumPy      | 1.24 - 2.2 |
| Pillow     | 9.5 - 11.x |
| Matplotlib | 3.7 - 3.10 |

You can also install dependencies manually:

```bash
pip install numpy pillow matplotlib
```
---

## Quick Start

1. **If you are NOT in the project's root directory**,\
   change the directory to the project's root directory:

   ```bash
   cd sbl_optimizer
   ```
   Note: make sure you are at ```sbl_optimizer``` not ```sbl_optimizer/sbl_optimizer```

2. Run the optimizer to generate an optimized pattern that accounts for heat diffusion:

   ```bash
   python -m sbl_optimizer.main sample.jpg
   ```

3. Locate the generated optimized pattern `sample_opt.pdf` in the project's root directory.

4. Check the simulated heat distribution `sample_temperature.png` and swell pattern `sample_swell.png`.

5. Print the `sample_opt.pdf` on paper, apply paste, and expose to a strong LED spotlight. Darker printed regions absorb more heat and swell.

6. Try optimizing your own pattern.
   
   ```bash
   python -m sbl_optimizer.main path/to/your_image
   ```

---

## Configuration

Some parameters can be customized via a JSON file (default: `config.json` shipped with the package).

`config.json`
```json
{
  "swell_temperature": 145.0,
  "light_power": 100.0,
  "light_diameter": 0.06,
  "alpha": 5e-07
}
```

| Key                 | Type   | Description                                                   |
|---------------------|--------|---------------------------------------------------------------|
| `swell_temperature` | float  | Target swelling temperature (°C).                             |
| `light_power`       | float  | Light source power (W).                                       |
| `light_diameter`    | float  | Diameter of the light circle on paper (m).                    |
| `alpha`             | float  | Thermal diffusivity of paper (m²/s).                          |

To override defaults:

```bash
python -m sbl_optimizer.main <IMAGE> --config path/to/your_config.json
```

---

## Command Line Interface

### Usage

```bash
python -m sbl_optimizer.main [OPTIONS] <IMAGE>
```

### Arguments

  `<IMAGE>`\
  Path to the input image (JPG, PNG, etc.)

### Options

| Option                  | Description                |
| ----------------------- | -------------------------- |
| `-c`, `--config <FILE>` | Path to JSON config file   |
| `-h`, `--help`          | Show help message and exit |

---

## Examples

1. Use default settings on `sample.jpg` in the project's root directory.
    ```bash
    python -m sbl_optimizer.main sample.jpg
    ```

2. Use custom settings
    ```bash
    python -m sbl_optimizer.main sample.jpg --config my_config.json
    ```

3. Save only error logs (disable plotting)\
    Edit `main.py`:
    - comment out `save_plots`, uncomment `save_errors`

Output files (in same folder as input image `sample.jpg`):

| File                      | Description                         |
| ------------------------- | ----------------------------------- |
| `sample_opt.pdf`         | Optimized pattern to be printed.    |
| `sample_temperature.png` | Simulated temperature distribution. |
| `sample_swell.png`       | Simulated swell pattern.            |

---

## Citation

If you use **sbl-optimizer** in your research or projects, please cite:

```bibtex
@inproceedings{10.1145/3689050.3704420,
author = {Ichihashi, Sosuke and Howell, Noura and Oh, HyunJoo},
title = {Swell by Light: An Approachable Technique for Freeform Raised Textures},
year = {2025},
isbn = {9798400711978},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3689050.3704420},
doi = {10.1145/3689050.3704420},
booktitle = {Proceedings of the Nineteenth International Conference on Tangible, Embedded, and Embodied Interaction},
articleno = {45},
numpages = {16},
keywords = {2.5D fabrication, Personal fabrication, tactile rendering},
location = {Bordeaux / Talence, France},
series = {TEI '25}
}
```

See the [paper](https://doi.org/10.1145/3689050.3704420) and [project page](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/) for more details.

---

## Contributing

Contributions, issues, and feature requests are welcome!  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am 'Add foo'`)  
4. Push to the branch (`git push origin feature/foo`)  
5. Open a Pull Request

Please follow the existing code style and write tests for new functionality.

---

## License

This project is licensed under the [MIT License](LICENSE).
