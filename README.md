<div align="center">

# 🐔 Détection de Maladies Aviaires par Vision par Ordinateur

**Dataset de 2 300+ images de volailles (saines / malades) pour l'entraînement de modèles de deep learning**

[![Python 3.12](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.13-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Roboflow](https://img.shields.io/badge/Roboflow-API-7B3FE4?logo=roboflow)](https://roboflow.com)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

</div>

---

## 📋 Table des Matières

- [Aperçu du Projet](#-aperçu-du-projet)
- [Structure du Projet](#-structure-du-projet)
- [Prérequis par OS](#-prérequis-par-os)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [macOS](#macos)
  - [Windows](#windows)
- [Installation](#-installation)
  - [1. Cloner le projet](#1-cloner-le-projet)
  - [2. Créer l'environnement virtuel](#2-créer-lenvironnement-virtuel)
  - [3. Activer l'environnement](#3-activer-lenvironnement)
  - [4. Installer les dépendances](#4-installer-les-dépendances)
  - [5. Configurer la clé API Roboflow](#5-configurer-la-clé-api-roboflow)
- [Téléchargement des Datasets](#-téléchargement-des-datasets)
- [Datasets Disponibles](#-datasets-disponibles)
- [Utilisation pour l'Entraînement](#-utilisation-pour-lentraînement)
- [Dépannage](#-dépannage)
- [Licences](#-licences)

---

## 🎯 Aperçu du Projet

Ce projet collecte et structure des **images de volailles (corps entier)** provenant de sources ouvertes (Roboflow Universe) pour entraîner un modèle de deep learning capable de détecter si une volaille est **saine** ou **malade** à partir d'une photo.

### Ce qui est inclus ✅
- **4 datasets** d'images corporelles de volailles (∼2 300+ images)
- Script de téléchargement automatique
- Structure organisée pour l'entraînement
- Documentation complète de chaque dataset

### Ce qui est exclu ❌
- ❌ Fientes / fèces / excréments
- ❌ Lésions d'organes internes
- ❌ Données microbiologiques

---

## 📂 Structure du Projet

```
📦 data-vik/
├── .env                    # 🔑 Clés API (NE PAS COMMITTER)
├── .env.example            # Template pour les clés API
├── .gitignore              # Fichiers ignorés par Git
├── README.md               # 👈 Ce fichier
├── requirements.txt        # Dépendances Python
├── rapport_complet.md      # Rapport détaillé des datasets
│
├── scripts/
│   └── download_all.py     # Script de téléchargement principal
│
├── docs/                   # Documentation individuelle des datasets
│   ├── 01_ROBOFLOW_POULTRY_DETECTION.md
│   ├── 02_ROBOFLOW_CHIKHEN.md
│   ├── 03_ROBOFLOW_DISEASE_PREDICTION.md
│   └── 04_ROBOFLOW_BROILER.md
│
├── datasets/               # 📁 Données téléchargées (généré)
│   ├── 01_poultry_detection_counter/
│   ├── 02_chikhen/
│   ├── 03_disease_prediction/
│   └── 04_broiler_health/
│
├── merged/                 # 📁 Données fusionnées sain/malade (vide)
│   ├── train/
│   ├── val/
│   └── test/
│
└── venv/                   # 🐍 Environnement virtuel (généré)
```

---

## 🖥️ Prérequis par OS

### Linux (Ubuntu/Debian)

```bash
# Python 3.12+ et pip
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

### macOS

```bash
# Option 1: Homebrew (recommandé)
brew install python@3.12

# Option 2: Official Python installer
# https://www.python.org/downloads/
```

### Windows

1. **Téléchargez Python 3.12+** : [python.org/downloads](https://www.python.org/downloads/)
   - ✅ **Cochez "Add Python to PATH"** pendant l'installation
   - Ou depuis PowerShell (avec [winget](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/)) :
     ```powershell
     winget install Python.Python.3.12
     ```

2. **Redémarrez PowerShell** après l'installation.

---

## 🚀 Installation

### Installation rapide (30 secondes)

Selon votre OS, exécutez l'une des commandes suivantes depuis le dossier du projet :

```bash
# Linux / macOS
bash setup.sh

# Windows (PowerShell)
# 1. Ouvrez PowerShell dans le dossier du projet
# 2. Exécutez :
.\setup.ps1
```

> ⚠️ Si vous êtes sur Windows et que PowerShell bloque l'exécution :
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Puis relancez `.\setup.ps1`

---

### Installation manuelle (pas à pas)

### 1. Cloner le projet

```bash
git clone <votre-repo-url> data-vik
cd data-vik
```

> **Sans Git** : Téléchargez le dossier et décompressez-le, puis ouvrez un terminal dans le dossier.

### 2. Créer l'environnement virtuel

```bash
# Linux / macOS
python3 -m venv venv

# Windows PowerShell
python -m venv venv
```

### 3. Activer l'environnement

```bash
# Linux / macOS (bash/zsh)
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Cmd)
venv\Scripts\activate.bat
```

> 💡 Vous devriez voir `(venv)` apparaître dans votre terminal.

### 4. Installer les dépendances

```bash
# Une fois le venv activé (voir étape 3)
pip install --upgrade pip
pip install -r requirements.txt
```

**Cela installe :**
| Package | Utilité |
|---------|---------|
| `torch` + `torchvision` | Deep learning (PyTorch) |
| `opencv-python-headless` | Traitement d'images |
| `roboflow` | Téléchargement des datasets |
| `numpy`, `pandas` | Analyse de données |
| `matplotlib`, `seaborn` | Visualisation |
| `scikit-learn` | Métriques ML |
| `albumentations` | Augmentation d'images |
| `jupyter` | Notebooks interactifs |
| `python-dotenv` | Chargement des clés API |

### 5. Configurer la clé API Roboflow

**5a. Créez un compte Roboflow** (gratuit)

👉 [https://app.roboflow.com/settings/api](https://app.roboflow.com/settings/api)

**5b. Copiez votre clé API**

Sur la page des paramètres, vous verrez votre clé qui commence par `rf_...`. Cliquez sur **Copier**.

**5c. Ajoutez la clé au fichier `.env`**

```bash
# Copiez le template
cp .env.example .env

# Éditez le fichier .env
nano .env   # ou vim, code, notepad, etc.
```

Remplacez :
```env
ROBOFLOW_API_KEY="rf_xxxx..."
```
par :
```env
ROBOFLOW_API_KEY="rf_votre_clé_copiée"
```

> **Alternative** : Vous pouvez aussi exporter la variable directement :
> ```bash
> # Linux / macOS
> export ROBOFLOW_API_KEY='rf_votre_clé'
>
> # Windows PowerShell
> $env:ROBOFLOW_API_KEY='rf_votre_clé'
>
> # Windows Cmd
> set ROBOFLOW_API_KEY=rf_votre_clé
> ```

---

## 📦 Téléchargement des Datasets

```bash
# Vérifier que le venv est activé (voir (venv) dans le terminal)
# Si non : source venv/bin/activate (Linux/macOS) ou .\venv\Scripts\Activate.ps1 (Windows)

# Lister les datasets disponibles
python scripts/download_all.py --list

# Télécharger les 4 datasets Roboflow
python scripts/download_all.py --roboflow-only

# Tout faire (téléchargement + documentation)
python scripts/download_all.py --all

# Générer uniquement la documentation
python scripts/download_all.py --docs-only
```

> ⏱️ Le téléchargement complet peut prendre plusieurs minutes selon votre connexion.

---

## 📊 Datasets Disponibles

| # | Dataset | Images | Classes | Contenu | Taille |
|---|---------|--------|---------|---------|--------|
| ⭐ | **Poultry Detection for Counter** | 1 268 | 18 | Corps entier + détails | 37 MB |
| 🐔 | **Chikhen** | 509 | 6 | Corps/tête/pattes | 39 MB |
| 🩺 | **Disease Prediction** | 30 | 2 | Corps entier | 1.4 MB |
| 🐤 | **Broiler Chicken Health** | 505 | 2 | Corps entier | 10 MB |
| | **📦 Total** | **2 312** | | | **88 MB** |

**Mapping des classes :**
- ✅ **healthy** → Volaille saine
- ❌ **sick** → Volaille malade

---

## 🧠 Utilisation pour l'Entraînement

```python
import torch
import torchvision.transforms as T
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

# Exemple : charger les données pour l'entraînement
transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]),
])

# Les datasets téléchargés sont au format YOLOv8
# Chaque dossier contient : train/ / valid/ / test/ + data.yaml
```

Les données téléchargées sont au format **YOLOv8** avec la structure suivante :
```
datasets/01_poultry_detection_counter/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── data.yaml    # Configuration des classes
```

---

## 🔧 Dépannage

### Problème : "ROBOFLOW_API_KEY non définie"
```bash
# Vérifiez que le fichier .env existe et est bien rempli
cat .env

# Ou vérifiez la variable d'environnement
echo $ROBOFLOW_API_KEY   # Linux/macOS
echo %ROBOFLOW_API_KEY%  # Windows Cmd
```

### Problème : "pip install" échoue
```bash
# Assurez-vous que pip est à jour
pip install --upgrade pip

# Sur Linux, si vous êtes en dehors du venv :
pip install --break-system-packages -r requirements.txt
```

### Problème : "Version number X is not found"
```bash
# Le script détecte automatiquement la dernière version.
# Relancez simplement :
python scripts/download_all.py --roboflow-only
```

### Problème : "roboflow package not installed"
```bash
pip install roboflow
```

### Problème : Permission denied sur Linux/macOS
```bash
chmod +x scripts/download_all.py
```

### Problème : Windows - "Activate.ps1 cannot be loaded"
```powershell
# Exécutez PowerShell en tant qu'Administrateur, puis :
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# Réessayez : .\venv\Scripts\Activate.ps1
```

---

## 📜 Licences

Chaque dataset a sa propre licence. Veuillez vérifier individuellement :

| Dataset | Licence |
|---------|---------|
| Poultry Detection for Counter | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Chikhen | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Disease Prediction | Roboflow Public |
| Broiler Chicken Healthy and Sick | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

---

<div align="center">

**Projet réalisé pour la collecte de données d'entraînement**  
🔬 *Détection de maladies aviaires par vision par ordinateur*

</div>
