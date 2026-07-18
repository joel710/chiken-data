# 🐔 Détection de Maladies Aviaires - Dataset Vision par Ordinateur

[![Python 3.12](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.13-EE4C2C?logo=pytorch)](https://pytorch.org)
[![Roboflow](https://img.shields.io/badge/Roboflow-API-7B3FE4)](https://roboflow.com)
[![Licence: CC BY 4.0](https://img.shields.io/badge/Licence-CC_BY_4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

---

## Table des Matières

- [Aperçu du Projet](#apercu-du-projet)
- [Structure du Projet](#structure-du-projet)
- [Prérequis par Système d'Exploitation](#prerequis-par-systeme-dexploitation)
  - [Linux (Ubuntu/Debian)](#linux-ubuntudebian)
  - [macOS](#macos)
  - [Windows](#windows)
- [Installation](#installation)
  - [Installation Rapide (30 secondes)](#installation-rapide-30-secondes)
  - [Installation Manuelle (pas à pas)](#installation-manuelle-pas-a-pas)
- [Téléchargement des Datasets](#telechargement-des-datasets)
- [Référence des Datasets](#reference-des-datasets)
- [Utilisation pour l'Entraînement](#utilisation-pour-lentrainement)
- [Dépannage](#depannage)
- [Licences](#licences)

---

## Aperçu du Projet

Ce projet collecte et structure des **images corporelles de volailles** (principalement des poulets) provenant de datasets open-source hébergés sur Roboflow Universe. L'objectif est de fournir un jeu de données prêt à l'emploi pour entraîner un modèle de deep learning capable de classifier si une volaille est **saine** ou **malade** à partir d'une photographie de son corps.

Les datasets inclus couvrent des images en corps entier de poulets, dindes et autres volailles, avec des annotations qui distinguent les états physiques sains des états anormaux. Cela inclut la qualité du plumage, la posture, l'état des pattes, l'apparence de la tête et l'aspect général de l'animal.

**Ce qui est inclus :**
- 4 datasets d'images corporelles de volailles (environ 2 300+ images au total)
- Un script de téléchargement automatisé avec authentification API et détection de version
- Une structure de dossiers organisée et prête pour l'entraînement
- Une documentation individuelle pour chaque dataset, incluant le mapping des classes et les métriques de performance connues

**Ce qui est exclu (par conception) :**
- Images de fientes et d'excréments
- Images de lésions d'organes internes
- Données microbiologiques ou de laboratoire
- Datasets Kaggle, Zenodo et Mendeley (non compatibles avec le workflow automatisé)

Les datasets sont téléchargés au format **YOLOv8**, qui comprend les images, les annotations et un fichier de configuration. Ce format est compatible avec la plupart des frameworks modernes de vision par ordinateur, notamment PyTorch, Ultralytics YOLO et TensorFlow.

---

## Structure du Projet

```
data-vik/
│
├── .env                      # Clés API (exclu du versionnement)
├── .env.example              # Template pour les clés API
├── .gitignore                # Règles d'exclusion Git
├── README.md                 # Ce fichier de documentation
├── requirements.txt          # Dépendances Python
├── rapport_complet.md        # Rapport d'analyse détaillé des datasets
│
├── scripts/
│   └── download_all.py       # Script principal de téléchargement
│
├── docs/
│   ├── 01_ROBOFLOW_POULTRY_DETECTION.md
│   ├── 02_ROBOFLOW_CHIKHEN.md
│   ├── 03_ROBOFLOW_DISEASE_PREDICTION.md
│   └── 04_ROBOFLOW_BROILER.md
│
├── datasets/                 # Données téléchargées (généré, exclu du git)
│   ├── 01_poultry_detection_counter/
│   ├── 02_chikhen/
│   ├── 03_disease_prediction/
│   └── 04_broiler_health/
│
├── merged/                   # Structure fusionnée (prête à l'emploi)
│   ├── train/
│   ├── val/
│   └── test/
│
├── setup.sh                  # Script d'installation automatisé (Linux/macOS)
├── setup.ps1                 # Script d'installation automatisé (Windows)
│
└── venv/                     # Environnement virtuel Python (généré)
```

---

## Prérequis par Système d'Exploitation

Avant de configurer le projet, vous devez disposer d'une installation fonctionnelle de **Python 3.12 ou plus récent** sur votre machine. Les sections ci-dessous détaillent les méthodes recommandées pour chaque système d'exploitation.

### Linux (Ubuntu/Debian)

Sur les distributions Linux basées sur Debian, Python s'installe via le gestionnaire de paquets :

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

Pour les autres distributions (Fedora, Arch, etc.), utilisez le gestionnaire de paquets correspondant.

### macOS

La méthode recommandée sur macOS est d'utiliser Homebrew, qui fournit une version récente de Python sans interférer avec le Python système :

```bash
brew install python@3.12
```

Vous pouvez également télécharger l'installateur officiel depuis [python.org/downloads](https://www.python.org/downloads/).

### Windows

1. Téléchargez Python 3.12 ou plus récent depuis le site officiel : [python.org/downloads](https://www.python.org/downloads/)
2. Pendant l'installation, veillez à **cocher l'option "Add Python to PATH"**.
3. Vous pouvez aussi installer Python via PowerShell avec le Windows Package Manager :
   ```powershell
   winget install Python.Python.3.12
   ```
4. Redémarrez votre terminal après l'installation pour que les changements de PATH prennent effet.

---

## Installation

### Installation Rapide (30 secondes)

Des scripts d'installation automatisés sont fournis pour gérer l'ensemble du processus, y compris la création de l'environnement virtuel et l'installation des dépendances.

**Linux et macOS :**
```bash
bash setup.sh
```

**Windows (PowerShell) :**
```powershell
.\setup.ps1
```

Si PowerShell bloque l'exécution du script, vous devrez peut-être ajuster la politique d'exécution au préalable :
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Le script d'installation effectue automatiquement les actions suivantes :
- Vérifie que Python est installé et accessible
- Crée un environnement virtuel Python dans le dossier `venv/`
- Installe toutes les dépendances requises depuis `requirements.txt`
- Copie `.env.example` vers `.env` si ce dernier n'existe pas déjà

Une fois le script terminé, vous devrez :
1. Éditer le fichier `.env` pour ajouter votre clé API Roboflow
2. Lancer la commande de téléchargement des datasets

### Installation Manuelle (pas à pas)

Si vous préférez configurer le projet manuellement, suivez les étapes ci-dessous.

#### 1. Cloner ou télécharger le projet

```bash
git clone <url-du-repo> data-vik
cd data-vik
```

Si vous avez téléchargé le projet en ZIP, extrayez-le et ouvrez un terminal dans le dossier.

#### 2. Créer un environnement virtuel

L'environnement virtuel isole les dépendances du projet de votre Python système, évitant ainsi les conflits de versions :

```bash
# Linux et macOS
python3 -m venv venv

# Windows (PowerShell)
python -m venv venv
```

#### 3. Activer l'environnement virtuel

L'activation de l'environnement rend les paquets installés disponibles pour vos sessions Python. Vous devriez voir le préfixe `(venv)` apparaître dans votre terminal.

```bash
# Linux et macOS (bash/zsh)
source venv/bin/activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Invite de commandes)
venv\Scripts\activate.bat
```

#### 4. Installer les dépendances

Une fois l'environnement virtuel activé, installez les paquets requis :

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient les paquets suivants :

| Paquet | Utilité |
|--------|---------|
| `torch` et `torchvision` | Framework deep learning (PyTorch) pour l'entraînement et l'évaluation |
| `opencv-python-headless` | Traitement d'images et opérations de vision par ordinateur |
| `roboflow` | Client API pour télécharger les datasets depuis Roboflow Universe |
| `numpy` et `pandas` | Calcul numérique et manipulation de données |
| `matplotlib` et `seaborn` | Visualisation de données et tracés |
| `scikit-learn` | Métriques d'apprentissage automatique et outils d'évaluation |
| `albumentations` | Augmentation d'images pour les données d'entraînement |
| `jupyter` | Notebooks interactifs pour l'exploration de données |
| `python-dotenv` | Chargement des variables d'environnement depuis le fichier `.env` |

#### 5. Configurer la clé API Roboflow

Les datasets sont hébergés sur Roboflow Universe et nécessitent une clé API pour le téléchargement. L'obtention d'une clé est gratuite.

**Étape 1 :** Créez un compte Roboflow gratuit sur [app.roboflow.com/settings/api](https://app.roboflow.com/settings/api).

**Étape 2 :** Sur la page des paramètres, localisez votre clé API (elle commence par `rf_`). Cliquez sur le bouton Copier.

**Étape 3 :** Créez et éditez le fichier `.env` à la racine du projet :

```bash
cp .env.example .env
```

Ouvrez le fichier `.env` avec un éditeur de texte :

```bash
nano .env   # ou vim, code, notepad, etc.
```

Remplacez la valeur fictive par votre clé API réelle :

```env
ROBOFLOW_API_KEY="rf_votre_cle_copice"
```

**Méthode alternative :** Si vous préférez ne pas utiliser de fichier `.env`, vous pouvez exporter la variable directement :

```bash
# Linux et macOS
export ROBOFLOW_API_KEY='rf_votre_cle'

# Windows (PowerShell)
$env:ROBOFLOW_API_KEY='rf_votre_cle'

# Windows (Invite de commandes)
set ROBOFLOW_API_KEY=rf_votre_cle
```

---

## Téléchargement des Datasets

Une fois l'environnement virtuel activé et la clé API configurée, vous pouvez télécharger les datasets à l'aide du script fourni.

**Lister les datasets disponibles sans télécharger :**

```bash
python scripts/download_all.py --list
```

Cette commande affiche les quatre datasets disponibles avec leur nombre d'images et de classes.

**Télécharger tous les datasets Roboflow :**

```bash
python scripts/download_all.py --roboflow-only
```

Pour chaque dataset, le script de téléchargement effectue les opérations suivantes :
1. Connexion à l'API Roboflow avec la clé configurée
2. Détection automatique de la dernière version du dataset
3. Téléchargement des données au format YOLOv8
4. Vérification de l'intégrité des fichiers téléchargés
5. Rapport du nombre d'images et de fichiers d'annotation

**Autres commandes disponibles :**

```bash
# Tout faire (téléchargement + documentation)
python scripts/download_all.py --all

# Générer uniquement les fichiers de documentation
python scripts/download_all.py --docs-only
```

Le volume total de téléchargement est d'environ **90 Mo**. Selon la vitesse de votre connexion internet, le processus peut prendre plusieurs minutes.

---

## Référence des Datasets

Le tableau ci-dessous résume les quatre datasets inclus dans ce projet. Chaque dataset contient des images de volailles capturées dans des conditions réelles, avec des variations d'éclairage, d'arrière-plan et d'angle de prise de vue.

| Dataset | Images | Classes | Contenu | Taille |
|---------|--------|---------|---------|--------|
| Poultry Detection for Counter | 1 268 | 18 | Corps entier, tête, pattes, plumage | 37 Mo |
| Chikhen | 509 | 6 | Corps, tête et pattes (normal vs anormal) | 39 Mo |
| Disease Prediction | 30 | 2 | Corps entier (Normal vs Anormal) | 1.4 Mo |
| Broiler Chicken Healthy and Sick | 505 | 2 | Corps entier (Sain vs Malade) | 10 Mo |
| **Total** | **2 312** | | | **88 Mo** |

**Note :** La vue liste (`--list`) affiche environ 9 145 images d'après les métadonnées des datasets. Le téléchargement via l'API retourne un sous-ensemble exploitable d'environ 2 312 images, qui correspond à la version préparée par les auteurs pour une utilisation directe en entraînement.

**Convention de mapping des classes :**

Les classes d'images de l'ensemble des datasets sont mappées vers une tâche de classification binaire :
- **healthy** (classe positive) - Volailles en condition physique normale
- **sick** (classe négative) - Volailles présentant des signes visibles de maladie ou d'anomalie

---

## Utilisation pour l'Entraînement

Les datasets sont téléchargés au format YOLOv8, compatible avec la plupart des frameworks de vision par ordinateur. Chaque dossier de dataset contient la structure suivante :

```
datasets/01_poultry_detection_counter/
├── train/
│   ├── images/       # Images d'entraînement
│   └── labels/       # Annotations au format YOLO
├── valid/
│   ├── images/       # Images de validation
│   └── labels/       # Annotations correspondantes
├── test/
│   ├── images/       # Images de test
│   └── labels/       # Annotations correspondantes
└── data.yaml         # Fichier de configuration (noms des classes, chemins)
```

**Exemple : Chargement des données pour un entraînement PyTorch**

L'extrait de code suivant montre comment charger les images pour entraîner un modèle de classification avec PyTorch :

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

**Fusion des datasets pour un ensemble d'entraînement unifié :**

Le dossier `merged/` est pré-configuré avec les sous-dossiers `train/`, `val/` et `test/` (actuellement vides). Vous pouvez l'utiliser comme destination pour combiner les images de plusieurs datasets en une structure unique de classification sain/malade.

---

## Dépannage

### ROBOFLOW_API_KEY non définie

Le script ne trouve pas votre clé API. Vérifiez que le fichier `.env` existe à la racine du projet et contient la clé correcte :

```bash
cat .env
```

Vous pouvez également vérifier si la variable d'environnement est correctement définie :

```bash
echo $ROBOFLOW_API_KEY     # Linux et macOS
echo %ROBOFLOW_API_KEY%    # Windows Invite de commandes
```

Si la clé est manquante, éditez le fichier `.env` ou exportez la variable manuellement comme décrit dans la section d'installation.

### Échec de l'installation pip

Des versions obsolètes de pip peuvent causer des échecs d'installation. Mettez à jour pip avant de réessayer :

```bash
pip install --upgrade pip
```

Sur les systèmes Linux, si vous installez en dehors d'un environnement virtuel, vous pourriez avoir besoin de :

```bash
pip install --break-system-packages -r requirements.txt
```

### Numéro de version introuvable

Le script détecte automatiquement la dernière version de chaque dataset. Si vous recevez une erreur liée à la version, il s'agit probablement d'un problème transitoire avec l'API. Relancez simplement la commande de téléchargement :

```bash
python scripts/download_all.py --roboflow-only
```

### Paquet roboflow non installé

Installez le paquet manuellement :

```bash
pip install roboflow
```

### Permission refusée (Linux et macOS)

Assurez-vous que le script a les permissions d'exécution :

```bash
chmod +x scripts/download_all.py
```

### Windows - PowerShell bloque l'exécution

Si PowerShell bloque le script d'installation avec une erreur de sécurité, ajustez la politique d'exécution :

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Réessayez ensuite les commandes d'installation ou d'activation.

---

## Licences

Chaque dataset inclus dans ce projet est régi par sa propre licence. Veuillez vérifier les conditions avant d'utiliser les données dans des applications commerciales.

| Dataset | Licence |
|---------|---------|
| Poultry Detection for Counter | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Chikhen | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Disease Prediction | Roboflow Public License |
| Broiler Chicken Healthy and Sick | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

La licence **CC BY 4.0** autorise le partage et l'adaptation du matériel pour tout usage, à condition de créditer correctement l'auteur. La **Roboflow Public License** autorise une utilisation non commerciale et de recherche ; pour un usage commercial, veuillez consulter les conditions spécifiques sur la page Roboflow Universe du dataset concerné.

---

## À Propos

Ce projet a été créé dans le but de collecter et structurer des données d'entraînement pour la détection de maladies aviaires par vision par ordinateur. Il fournit un pipeline reproductible d'acquisition de datasets, qui pourra être étendu avec des sources supplémentaires à l'avenir.

Pour toute question ou contribution, veuillez ouvrir une issue ou une pull request sur le dépôt.
