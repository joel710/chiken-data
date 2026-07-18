# Poultry Disease Detection - Computer Vision Dataset

[![Python 3.12](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.13-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Roboflow](https://img.shields.io/badge/Roboflow-API-7B3FE4)](https://roboflow.com)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites by Operating System](#prerequisites-by-operating-system)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [macOS](#macos)
  - [Windows](#windows)
- [Installation](#installation)
  - [Quick Setup (30 seconds)](#quick-setup-30-seconds)
  - [Manual Installation (step by step)](#manual-installation-step-by-step)
- [Downloading the Datasets](#downloading-the-datasets)
- [Dataset Reference](#dataset-reference)
- [Using the Data for Training](#using-the-data-for-training)
- [Troubleshooting](#troubleshooting)
- [Licenses](#licenses)

## Project Overview

This project collects and structures bird body images (primarily chickens) from open-source datasets hosted on Roboflow Universe. Its purpose is to provide a ready-to-use dataset for training a deep learning model capable of classifying whether a poultry bird is healthy or sick based on a photograph of its body.

The datasets included cover whole-body images of chickens, turkeys, and related poultry, with annotations that distinguish between healthy and abnormal physical states, including plumage quality, posture, leg conditions, and overall appearance.

**What is included:**
- 4 datasets of poultry body images (approximately 2,300+ images in total)
- An automated download script that handles API authentication and version detection
- Organized directory structure ready for model training
- Individual documentation for each dataset, including class mappings and known performance metrics

**What is excluded (by design):**
- Fecal and droppings imagery
- Internal organ lesion images
- Microbiological or laboratory data
- Kaggle, Zenodo, and Mendeley datasets (not compatible with the automated workflow)

The datasets are downloaded in YOLOv8 format, which includes images, annotation labels, and a data configuration file. This format is compatible with most modern object detection and classification frameworks, including PyTorch, Ultralytics YOLO, and TensorFlow.

## Project Structure

```
data-vik/
│
├── .env                      # API keys configuration file (excluded from version control)
├── .env.example              # Template for API keys setup
├── .gitignore                # Git exclusion rules
├── README.md                 # This documentation file
├── requirements.txt          # Python dependencies
├── rapport_complet.md        # Detailed dataset analysis report (in French)
│
├── scripts/
│   └── download_all.py       # Main download script with automatic version detection
│
├── docs/
│   ├── 01_ROBOFLOW_POULTRY_DETECTION.md
│   ├── 02_ROBOFLOW_CHIKHEN.md
│   ├── 03_ROBOFLOW_DISEASE_PREDICTION.md
│   └── 04_ROBOFLOW_BROILER.md
│
├── datasets/                 # Downloaded data (auto-generated, excluded from git)
│   ├── 01_poultry_detection_counter/
│   ├── 02_chikhen/
│   ├── 03_disease_prediction/
│   └── 04_broiler_health/
│
├── merged/                   # Merged dataset structure (empty, ready for use)
│   ├── train/
│   ├── val/
│   └── test/
│
├── setup.sh                  # Automated setup script for Linux and macOS
├── setup.ps1                 # Automated setup script for Windows PowerShell
│
└── venv/                     # Python virtual environment (auto-generated)
```

## Prerequisites by Operating System

Before setting up the project, you need a working Python 3.12 or newer installation on your machine. Below are the recommended ways to install Python for each major operating system.

### Linux (Ubuntu/Debian)

On Debian-based Linux distributions, Python can be installed using the package manager:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

For other distributions (Fedora, Arch, etc.), use the corresponding package manager. Python 3.12 or later is required.

### macOS

The recommended approach on macOS is to use Homebrew, which provides an up-to-date Python version without interfering with the system Python:

```bash
brew install python@3.12
```

Alternatively, you can download the official Python installer from [python.org/downloads](https://www.python.org/downloads/).

### Windows

1. Download Python 3.12 or later from the official website: [python.org/downloads](https://www.python.org/downloads/)
2. During installation, make sure to check the option **"Add Python to PATH"**.
3. Alternatively, you can install Python via PowerShell using the Windows Package Manager:
   ```powershell
   winget install Python.Python.3.12
   ```
4. After installation, restart your terminal for the PATH changes to take effect.

## Installation

### Quick Setup (30 seconds)

Automated scripts are provided to handle the entire installation process, including virtual environment creation and dependency installation.

**Linux and macOS:**
```bash
bash setup.sh
```

**Windows (PowerShell):**
```powershell
.\setup.ps1
```

If PowerShell blocks script execution on Windows, you may need to adjust the execution policy first:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then run the setup script again.

The setup script will perform the following actions automatically:
- Check that Python is installed and available
- Create a Python virtual environment in the `venv/` directory
- Install all required dependencies from `requirements.txt`
- Copy `.env.example` to `.env` if it does not already exist

After the script completes, you will need to:
1. Edit the `.env` file to add your Roboflow API key (see step 5 below)
2. Run the dataset download command

### Manual Installation (step by step)

If you prefer to set up the project manually, follow the steps below.

#### 1. Clone or download the project

```bash
git clone <repository-url> data-vik
cd data-vik
```

If you downloaded the project as a ZIP archive, extract it and navigate to the project directory in your terminal.

#### 2. Create a virtual environment

A virtual environment isolates the project dependencies from your system Python, preventing version conflicts:

```bash
# Linux and macOS
python3 -m venv venv

# Windows (PowerShell)
python -m venv venv
```

#### 3. Activate the virtual environment

Activating the environment makes the installed packages available to your Python sessions. You should see the `(venv)` prefix appear in your terminal prompt.

```bash
# Linux and macOS (bash/zsh)
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat
```

#### 4. Install dependencies

With the virtual environment activated, install the required packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

The `requirements.txt` file includes the following packages and their purposes:

| Package | Purpose |
|---------|---------|
| `torch` and `torchvision` | Deep learning framework (PyTorch) for model training and evaluation |
| `opencv-python-headless` | Image processing and computer vision operations |
| `roboflow` | API client for downloading datasets from Roboflow Universe |
| `numpy` and `pandas` | Numerical computation and data manipulation |
| `matplotlib` and `seaborn` | Data visualization and plotting |
| `scikit-learn` | Machine learning metrics and evaluation tools |
| `albumentations` | Image augmentation for training data |
| `jupyter` | Interactive notebooks for data exploration |
| `python-dotenv` | Environment variable loading from `.env` files |

#### 5. Configure the Roboflow API key

The datasets are hosted on Roboflow Universe and require an API key for download. Obtaining a key is free.

**Step 1:** Create a free Roboflow account at [app.roboflow.com/settings/api](https://app.roboflow.com/settings/api).

**Step 2:** On the settings page, locate your API key (it starts with `rf_`). Click the copy button.

**Step 3:** Create and edit the `.env` file in the project root:

```bash
cp .env.example .env
```

Open the `.env` file with a text editor:

```bash
nano .env   # or vim, code, notepad, etc.
```

Replace the placeholder value with your actual API key:

```env
ROBOFLOW_API_KEY="rf_your_copied_key_here"
```

**Alternative method:** If you prefer not to use a `.env` file, you can export the key as an environment variable directly:

```bash
# Linux and macOS
export ROBOFLOW_API_KEY='rf_your_key'

# Windows (PowerShell)
$env:ROBOFLOW_API_KEY='rf_your_key'

# Windows (Command Prompt)
set ROBOFLOW_API_KEY=rf_your_key
```

## Downloading the Datasets

Once the virtual environment is activated and the API key is configured, you can download the datasets using the provided script.

**List available datasets without downloading:**

```bash
python scripts/download_all.py --list
```

This command displays the four available datasets with their image counts and class numbers.

**Download all datasets from Roboflow:**

```bash
python scripts/download_all.py --roboflow-only
```

The download script performs the following operations for each dataset:
1. Connects to the Roboflow API using your configured API key
2. Detects the latest version of each dataset automatically
3. Downloads the data in YOLOv8 format
4. Verifies that the files were written correctly
5. Reports the count of downloaded images and annotation files

**Other available commands:**

```bash
# Download datasets and generate documentation
python scripts/download_all.py --all

# Generate only the documentation files
python scripts/download_all.py --docs-only
```

The total download size is approximately 90 MB. Depending on your internet connection speed, the process may take several minutes.

## Dataset Reference

The following table summarizes the four datasets included in this project. Each dataset contains poultry body images captured in real-world conditions, with variations in lighting, background, and camera angles.

| Dataset | Images | Classes | Content | Size |
|---------|--------|---------|---------|------|
| Poultry Detection for Counter | 1 268 | 18 | Full body, head, legs, plumage details | 37 MB |
| Chikhen | 509 | 6 | Body, head, and feet (normal vs abnormal) | 39 MB |
| Disease Prediction | 30 | 2 | Whole body (Normal vs Abnormal) | 1.4 MB |
| Broiler Chicken Healthy and Sick | 505 | 2 | Whole body (Healthy vs Sick) | 10 MB |
| **Total** | **2 312** | | | **88 MB** |

**Note:** The list view (`--list`) shows approximately 9,145 images based on the dataset metadata. The actual API download returns a usable subset of approximately 2,312 images, which is the version that the authors have prepared for direct use in model training.

**Class mapping convention:**

The image classes across all datasets are mapped to a binary classification task:
- **healthy** (positive class) - Poultry birds in normal physical condition
- **sick** (negative class) - Birds showing visible signs of disease or abnormality

## Using the Data for Training

The datasets are downloaded in the YOLOv8 format, which is compatible with most computer vision frameworks. Each dataset directory contains the following structure:

```
datasets/01_poultry_detection_counter/
├── train/
│   ├── images/       # Training images
│   └── labels/       # Annotation labels in YOLO format
├── valid/
│   ├── images/       # Validation images
│   └── labels/       # Corresponding annotations
├── test/
│   ├── images/       # Test images
│   └── labels/       # Corresponding annotations
└── data.yaml         # Dataset configuration file (class names, paths)
```

**Example: Loading the data for PyTorch training**

The following code snippet demonstrates how to load the images for training a classification model using PyTorch:

```python
import torch
import torchvision.transforms as T
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]),
])

dataset = ImageFolder(
    root="datasets/01_poultry_detection_counter/train/images",
    transform=transform
)

dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

**Merging datasets for a unified training set:**

The `merged/` directory is pre-configured with `train/`, `val/`, and `test/` subdirectories (currently empty). You can use it as a destination when combining images from multiple datasets into a single healthy/sick classification structure.

## Troubleshooting

### ROBOFLOW_API_KEY not defined

The script cannot find your API key. Verify that the `.env` file exists in the project root and contains the correct key:

```bash
cat .env
```

Alternatively, check whether the environment variable is set correctly:

```bash
echo $ROBOFLOW_API_KEY     # Linux and macOS
echo %ROBOFLOW_API_KEY%    # Windows Command Prompt
```

If the key is missing, either edit the `.env` file or export the variable manually as described in the installation section.

### pip installation fails

Outdated pip versions can cause installation failures. Update pip before retrying:

```bash
pip install --upgrade pip
```

On Linux systems, if you are installing outside a virtual environment, you may need:

```bash
pip install --break-system-packages -r requirements.txt
```

### Version number not found

The script automatically detects the latest version of each dataset. If you receive a version-related error, it is likely a transient API issue. Simply re-run the download command:

```bash
python scripts/download_all.py --roboflow-only
```

### roboflow package not installed

Install the package manually:

```bash
pip install roboflow
```

### Permission denied (Linux and macOS)

Ensure the script has execution permissions:

```bash
chmod +x scripts/download_all.py
```

### Windows PowerShell execution policy

If PowerShell blocks the setup script with a security error, adjust the execution policy:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then retry the setup or activation commands.

## Licenses

Each dataset included in this project is governed by its own license. Please review the terms before using the data in commercial applications.

| Dataset | License |
|---------|---------|
| Poultry Detection for Counter | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Chikhen | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Disease Prediction | Roboflow Public License |
| Broiler Chicken Healthy and Sick | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

The CC BY 4.0 license allows sharing and adaptation of the material for any purpose, provided appropriate credit is given. The Roboflow Public License permits non-commercial and research use; for commercial use, please check the specific terms on the Roboflow Universe page for that dataset.

## About

This project was created for the purpose of collecting and structuring training data for poultry disease detection using computer vision. It provides a reproducible pipeline for dataset acquisition that can be extended with additional sources in the future.

For questions or contributions, please open an issue or pull request on the repository.
