<!-- Language Selector -->
[🔤 English](#sbl-optimizer) | [🇯🇵 日本語](#sbl-optimizer-日本語)

# sbl-optimizer

[![License](https://img.shields.io/badge/license-MIT-750014)](https://github.com/sosucat/sbl-optimizer/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/sbl-optimizer.svg)](https://badge.fury.io/py/sbl-optimizer)
[![GitHub](https://img.shields.io/badge/GitHub_repo-black?logo=github)](https://github.com/sosucat/sbl-optimizer)
[![Simple Colab](https://img.shields.io/badge/Easy_Colab-black?logo=googlecolab)](https://colab.research.google.com/drive/1Kpvq15wZrzsnQI28_JfkDSqCwT1ouyxj?usp=sharing)
[![Advanced Colab](https://img.shields.io/badge/Advanced_Colab-black?logo=googlecolab)](https://colab.research.google.com/drive/1KX5W0MG34zS_qX7RqeMLizrkhlWp8ojh?usp=sharing)\
[![Homepage](https://img.shields.io/badge/🔗_Homepage-black)](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/)
[![Fabrication Tutorial](https://img.shields.io/badge/🔗_Fabrication_tutorial-black)](https://sites.gatech.edu/futurefeelings/2025/08/06/make-puffy-patterns-with-light-advanced/)
[![Author](https://img.shields.io/badge/Author-black?logo=googlescholar&logoColor=white)](https://sosuke-ichihashi.com/)
[![Research paper](https://img.shields.io/badge/Research_Paper-black?logo=acm)](https://doi.org/10.1145/3689050.3704420)
[![Watch fabrication demo on YouTube](https://img.shields.io/badge/Fabrication-750014?logo=youtube)](https://youtu.be/LomVS_jHxl0?feature=shared)

Print pattern optimizer for ``Swell by Light (SbL)``.\
[SbL](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/) is an approachable technique for freeform raised textures on paper and other materials. SbL-Optimizer improves print patterns considering heat diffusion, making the resulting swell patterns better match the original images.

![Swell by Light](https://sites.gatech.edu/futurefeelings/files/2025/08/fab_process_short_opt.gif)

![A printed pattern's shades change as the optimization progresses, and the resulting temperature distribution gets closer to the intended pattern.](https://sites.gatech.edu/futurefeelings/files/2025/03/opt_step.gif)

Optimization of the printed pattern results in a uniform temperature pattern closely matching the original pattern.

---

## Table of Contents

- [sbl-optimizer](#sbl-optimizer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [1. (Recommended) From PyPI](#1-recommended-from-pypi)
    - [2. (Alternative) From Source](#2-alternative-from-source)
    - [Requirements](#requirements)
  - [Quick Start](#quick-start)
  - [Command Line Interface](#command-line-interface)
    - [Usage](#usage)
    - [Arguments](#arguments)
    - [Options](#options)
  - [Configuration](#configuration)
  - [Examples](#examples)
  - [Citation](#citation)
  - [License](#license)
- [sbl-optimizer 日本語](#sbl-optimizer-日本語)
  - [目次](#目次)
  - [特徴](#特徴)
  - [インストール](#インストール)
    - [1. （推奨）PyPI から](#1-推奨pypi-から)
    - [2. ソースから](#2-ソースから)
    - [必要条件](#必要条件)
  - [クイックスタート](#クイックスタート)
  - [コマンドラインインターフェース](#コマンドラインインターフェース)
    - [使用方法](#使用方法)
    - [引数](#引数)
    - [オプション](#オプション)
  - [設定](#設定)
  - [使用例](#使用例)
  - [引用](#引用)
  - [ライセンス](#ライセンス)

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

### 2. (Alternative) From Source
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

## License

This project is licensed under the [MIT License](LICENSE).\



---

# sbl-optimizer 日本語

[![ライセンス](https://img.shields.io/badge/license-MIT-750014)](https://github.com/sosucat/sbl-optimizer/blob/main/LICENSE)
[![PyPI バージョン](https://badge.fury.io/py/sbl-optimizer.svg)](https://badge.fury.io/py/sbl-optimizer)
[![GitHub](https://img.shields.io/badge/GitHub_repo-black?logo=github)](https://github.com/sosucat/sbl-optimizer?tab=readme-ov-file#sbl-optimizer-%E6%97%A5%E6%9C%AC%E8%AA%9E)
[![簡易版 Colab](https://img.shields.io/badge/簡易版Colab-black?logo=googlecolab)](https://colab.research.google.com/drive/15zYmaNvh88jztUcqpzwLXtT4YMRk2i1G?usp=sharing)
[![上級版 Colab](https://img.shields.io/badge/上級版Colab-black?logo=googlecolab)](https://colab.research.google.com/drive/1GLLGjPD7EhUV6evPHUeh6qHe3aNMV47u?usp=sharing)\
[![ホームページ](https://img.shields.io/badge/🔗_ホームページ-black)](https://sites.gatech.edu/futurefeelings/2025/07/03/swell-by-light-tei-25-2/)
[![製作チュートリアル](https://img.shields.io/badge/🔗_製作チュートリアル-black)](https://sites.gatech.edu/futurefeelings/2025/08/07/%e5%85%89%e3%81%a7%e3%83%87%e3%82%b3%e3%83%9c%e3%82%b3%e6%a8%a1%e6%a7%98%e3%82%92%e4%bd%9c%e3%82%8b%ef%bc%88%e4%b8%8a%e7%b4%9a%e7%b7%a8%ef%bc%89/)
[![著者](https://img.shields.io/badge/Author-black?logo=googlescholar&logoColor=white)](https://sosuke-ichihashi.com/)
[![英語論文](https://img.shields.io/badge/英語論文-black?logo=acm)](https://doi.org/10.1145/3689050.3704420)
[![YouTube で製作デモを見る](https://img.shields.io/badge/製作デモ-750014?logo=youtube)](https://youtu.be/LomVS_jHxl0?feature=shared)

``Swell by Light (熱光学式2.5次元印刷)`` 用の印刷パターン最適化ツールです。\
[Swell by Light](https://sites.gatech.edu/futurefeelings/2025/07/03/swell-by-light-tei-25-2/) は、紙やその他の素材に自由な形のデコボコ模様を作るための手軽な技術です。sbL-optimizer は熱伝導などを考慮して模様の濃淡を調節し、できあがるデコボコ模様を元画像の模様により近づけます。

![Swell by Light](https://sites.gatech.edu/futurefeelings/files/2025/08/fab_process_short_opt.gif)

![最適化の進行に伴い、印刷パターンの濃淡が変化し、得られる温度分布が目標パターンに近づく様子。](https://sites.gatech.edu/futurefeelings/files/2025/03/opt_step.gif)

模様の濃淡の最適化により、元画像の模様に近い均一な温度分布が得られます。

---

## 目次

- [sbl-optimizer](#sbl-optimizer)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [1. (Recommended) From PyPI](#1-recommended-from-pypi)
    - [2. (Alternative) From Source](#2-alternative-from-source)
    - [Requirements](#requirements)
  - [Quick Start](#quick-start)
  - [Command Line Interface](#command-line-interface)
    - [Usage](#usage)
    - [Arguments](#arguments)
    - [Options](#options)
  - [Configuration](#configuration)
  - [Examples](#examples)
  - [Citation](#citation)
  - [License](#license)
- [sbl-optimizer 日本語](#sbl-optimizer-日本語)
  - [目次](#目次)
  - [特徴](#特徴)
  - [インストール](#インストール)
    - [1. （推奨）PyPI から](#1-推奨pypi-から)
    - [2. ソースから](#2-ソースから)
    - [必要条件](#必要条件)
  - [クイックスタート](#クイックスタート)
  - [コマンドラインインターフェース](#コマンドラインインターフェース)
    - [使用方法](#使用方法)
    - [引数](#引数)
    - [オプション](#オプション)
  - [設定](#設定)
  - [使用例](#使用例)
  - [引用](#引用)
  - [ライセンス](#ライセンス)

---

## 特徴

- **熱伝導を考慮した模様最適化**  
  熱伝導・放射などを考慮し、元画像通りのデコボコ模様ができるように模様の濃淡を調整。
- **シンプルなコマンドラインインターフェース (CLI)**  
  JSON ベースの設定と画像入力でワンコマンド実行。
- **Python ベース**  
  NumPy、Pillow、Matplotlib を使用した計算・可視化。

---

## インストール
`sbl-optimizer` は以下の 2 つの方法でインストールできます。

### 1. （推奨）PyPI から

```bash
pip install sbl-optimizer
```

### 2. ソースから
リポジトリをクローンしてローカルにインストールします。

```bash
git clone https://github.com/sosucat/sbl-optimizer.git
cd sbl-optimizer
pip install .
```

### 必要条件

Python と以下のライブラリが必要です：
| ライブラリ   | バージョン    |
| ------------ | ------------- |
| Python       | 3.9 – 3.11    |
| NumPy        | 1.24 - 2.2    |
| Pillow       | 9.5 - 11.x    |
| Matplotlib   | 3.7 - 3.10    |

自動でインストールされなかった場合は手動でインストールしてください。

```bash
pip install numpy pillow matplotlib
```
---

## クイックスタート

1. サンプル画像で最適化を実行します：

   ```bash
   sbl-optimizer
   ```

2. 現在のディレクトリに生成された最適化された模様 `sample_opt.pdf` をチェック。

3. シミュレートされた温度分布 `sample_temperature.png` とデコボコ模様 `sample_swell.png` をチェック。

4. `sample_opt.pdf` を印刷し、熱膨張ペーストを塗り、強力な LED スポットライトを照射。模様通りのデコボコが出てきます。

5. 自分の模様画像を最適化してみましょう。
   
   ```bash
   sbl-optimizer path/to/your_image.png
   ```

---

## コマンドラインインターフェース

### 使用方法

```bash
sbl-optimizer [OPTIONS] <IMAGE>
```

### 引数

  `<IMAGE>`\
  入力画像のパス（JPG, PNG）

### オプション

| オプション               | 説明                                   |
| ------------------------ | -------------------------------------- |
| `-c`, `--config <FILE>`  | JSON 設定ファイルのパス                |
| `-h`, `--help`           | ヘルプメッセージを表示して終了         |

---

## 設定

一部のパラメータは JSON ファイル（デフォルト：パッケージ付属の `config.json`）でカスタマイズできます。

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

| キー                  | 型     | 説明                                                                                             |
|-----------------------|--------|--------------------------------------------------------------------------------------------------|
| `swell_temperature`   | float  | 膨張温度 [C°]。使用する膨張ペーストに記載されている、ペーストが膨らみ始める温度に応じて調整してください。 |
| `light_power`         | float  | 光出力 [W]。使用するライトの出力に応じて調節してください。                                         |
| `light_diameter`      | float  | 紙面に当たる光の直径 [m]。紙に光を当てて加熱する際に、光が当たる範囲に応じて調整してください。      |
| `alpha`               | float  | 紙の熱流量 [m²/s]。厚紙や極端に薄い紙などを使用する際に調節してください。                          |
| `verbose`             | int    | ログ出力の有無。 0：ログなし。 1: ログあり。                                                      |
| `resolution`          | int    | 熱シミュレーションの解像度。解像度を下げれば、最適化速度が上がる。解像度を上げれば、より画像に忠実なデコボコ模様になる。 |

カスタム設定で実行するには：

```bash
sbl-optimizer --config path/to/your_config.json <IMAGE>
```

---

## 使用例

1. サンプル画像をデフォルト設定で最適化
    ```bash
    sbl-optimizer
    ```

2. 自前の画像をデフォルト設定で最適化
    ``` bash
    sbl-optimizer flower.jpg
    ```

3. サンプル画像をカスタム設定で最適化
    ```bash
    sbl-optimizer --config my_config.json
    ```
   ``my_config.json`` の例：
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

出力ファイル（入力画像 `sample.jpg` と同じフォルダ）：

| ファイル名                   | 説明                               |
| ---------------------------- | ---------------------------------- |
| `sample_opt.pdf`             | 印刷用の最適化された模様。            |
| `sample_temperature.png`     | シミュレートされた温度分布。        |
| `sample_swell.png`           | シミュレートされたデコボコ模様。    |

---

## 引用

研究やプロジェクトで **sbl-optimizer** を使用する場合は、以下を引用してください。

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

詳細は [論文](https://doi.org/10.1145/3689050.3704420) および [プロジェクトページ](https://sites.gatech.edu/futurefeelings/2025/03/07/swell-by-light-tei-25/) を参照してください。

---


## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下で公開されています。
