# sbl-optimizer

[![License](https://img.shields.io/badge/license-MIT-750014)](https://doi.org/10.1145/3689050.3704420)
[![PyPI version](https://badge.fury.io/py/sbl-optimizer.svg)](https://badge.fury.io/py/sbl-optimizer)
[![GitHub](https://img.shields.io/badge/GitHub_repo-black?logo=github)](https://github.com/sosucat/sbl-optimizer)
[![Google colab](https://img.shields.io/badge/Google_Colab-black?logo=googlecolab)](https://github.com/sosucat/sbl-optimizer)\
[![Homepage](https://img.shields.io/badge/🔗_Homepage-black)](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/)
[![Author](https://img.shields.io/badge/Author-black?logo=googlescholar&logoColor=white)](https://sosuke-ichihashi.com/)
[![Research paper](https://img.shields.io/badge/Research_Paper-black?logo=acm)](https://doi.org/10.1145/3689050.3704420)
[![Watch fabrication demo on YouTube](https://img.shields.io/badge/Fabrication-750014?logo=youtube)](https://youtu.be/LomVS_jHxl0?feature=shared)

![Swell by Light](https://sites.gatech.edu/futurefeelings/files/2025/08/fab_process_full.gif)

Print pattern optimizer for ``Swell by Light (SbL)``.\
SbL is an approachable technique for freeform raised textures on paper and other materials. SbL-Optimizer improves print patterns considering heat diffusion, making the resulting swell patterns better match the original images.

````![A printed pattern's shades change as the optimization progresses, and the resulting temperature distribution gets closer to the intended pattern.](https://sites.gatech.edu/futurefeelings/files/2025/03/opt_step.gif)````

Optimization of the printed pattern results in a uniform temperature pattern closely matching the original pattern.

---

## Table of Contents

- [sbl-optimizer](#sbl-optimizer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [1. (Recommended) From PyPI](#1-recommended-from-pypi)
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
  Uses NumPy, Pillow, and Matplotlib for computations and visualizations.

---

## Installation
Install `sbl-optimizer` in two easy ways:

### 1. (Recommended) From PyPI

```bash
pip install sbl-optimizer
```

### 2. From Source
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

You can also install dependencies manually if they were not installed automatically:

```bash
pip install numpy pillow matplotlib
```
---

## Quick Start

1. Run the optimizer with a sample image:

   ```bash
   sbl-optimizer
   ```

2. Locate the generated optimized pattern `sample_opt.pdf` in the current directory.

3. Check the simulated temperature distribution `sample_temperature.png` and swell pattern `sample_swell.png`.

4. Print the `sample_opt.pdf` on paper, apply paste, and expose to a strong LED spotlight. Darker printed regions absorb more heat and swell.

5. Try optimizing your own pattern.
   
   ```bash
   sbl-optimizer path/to/your_image.png
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
  "alpha": 5e-07,
  "verbose": 1,
  "resolution": 120000
}
```

| Key                 | Type   | Description                                                   |
|---------------------|--------|---------------------------------------------------------------|
| `swell_temperature` | float  | Target swelling temperature (°C). Adjust this based on the swell temperature of the paste you have.                            |
| `light_power`       | float  | Light source power (W). Adjust this according to your light's power.                                      |
| `light_diameter`    | float  | Diameter of the light circle on paper (m). Adjust based on the light circle diameter during heating.                   |
| `alpha`             | float  | Thermal diffusivity of paper (m²/s).                          |
| `verbose`           | int    | Bool enabling logging. 0: turned off; 1: turned on.           |
| `resolution`        | int    | Number of cells paper is divided into in thermal simulations. Reduce this for faster optimization. Increase for a finer result.|

To override defaults:

```bash
sbl-optimizer --config path/to/your_config.json <IMAGE>
```

---

## Command Line Interface

### Usage

```bash
sbl-optimizer [OPTIONS] <IMAGE>
```

### Arguments

  `<IMAGE>`\
  Path to the input image (JPG, PNG)

### Options

| Option                  | Description                |
| ----------------------- | -------------------------- |
| `-c`, `--config <FILE>` | Path to JSON config file   |
| `-h`, `--help`          | Show help message and exit |

---

## Examples

1. Use default settings on a sample image.
    ```bash
    sbl-optimizer
    ```

2. Use default settings on your image.
    ```bash
    sbl-optimizer flower.jpg
    ```

3. Use custom settings
    ```bash
    sbl-optimizer --config my_config.json
    ```
    , where ``my_config.json`` looks like this:
    ```json
    {
    "swell_temperature": 135.0,
    "light_power": 120.0,
    "light_diameter": 0.07,
    "alpha": 5e-07,
    "verbose": 0,
    "resolution": 50000
    }
    ```

Output files (in same folder as input image `sample.jpg`):

| File                      | Description                         |
| ------------------------- | ----------------------------------- |
| `sample_opt.pdf`         | Optimized pattern to be printed.    |
| `sample_temperature.png` | Simulated temperature distribution. |
| `sample_swell.png`       | Simulated swell pattern.            |

---

## Citation

If you use **sbl-optimizer** in your research or projects, please cite:

Sosuke Ichihashi, Noura Howell, and HyunJoo Oh. 2025.\
Swell by Light: An Approachable Technique for Freeform Raised Textures. \
In Proceedings of the Nineteenth International Conference on Tangible, Embedded, and Embodied Interaction (TEI '25). Association for Computing Machinery, New York, NY, USA, Article 45, 1–16. https://doi.org/10.1145/3689050.3704420

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
