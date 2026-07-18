# Rapport Complet : Datasets pour la Détection de Maladies Aviaires par Vision par Ordinateur

> **Date :** 18 juillet 2026
> **Objectif :** Collecter des données ouvertes pour entraîner un modèle de détection de volailles malades vs saines **à partir d'images du sujet** (corps, tête, pattes)

---

## Table des Matières

1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Liste des Datasets Retenus](#2-liste-des-datasets-retenus)
3. [Poultry Detection for Counter ⭐](#3-poultry-detection-for-counter-)
4. [Disease Prediction](#4-disease-prediction)
5. [Chikhen Dataset](#5-chikhen-dataset)
6. [Broiler Chicken Healthy and Sick](#6-broiler-chicken-healthy-and-sick)
7. [Comparatif et Analyse](#7-comparatif-et-analyse)
8. [Guide de Téléchargement](#8-guide-de-téléchargement)
9. [Structure de Données Recommandée](#9-structure-de-données-recommandée)
10. [Considérations Éthiques et Légales](#10-considérations-éthiques-et-légales)

---

## 1. Résumé Exécutif

| Métrique | Valeur |
|----------|--------|
| **Datasets retenus** | 4 (tous sur Roboflow Universe) |
| **Volume total** | **~9 145 images** de volailles (corps, tête, pattes) |
| **Classification cible** | Sain 🟢 vs Malade 🔴 |
| **Format** | YOLO bounding boxes |
| **Licences** | CC BY 4.0 (ouverts) |
| **Accès** | Clé API Roboflow requise (gratuite) |

> ✅ **Tous les datasets exclus** : datasets de fientes, lésions, Kaggle fécaux, Zenodo, Mendeley, Hugging Face.

---

## 2. Liste des Datasets Retenus

| # | Dataset | Volume | Classes | Source | Priorité |
|---|---------|--------|---------|--------|----------|
| 1 | **Poultry Detection for Counter** ⭐ | **7 500** | 18 (sain/malade) | [Roboflow](https://universe.roboflow.com/mohamed-f-abdelshafie/poultry-detection-for-counter) | 🔴 Base principale |
| 2 | **Disease Prediction** | **1 200** | 2 (Normal/AbNormal) | [Roboflow](https://universe.roboflow.com/chicken-disease/disease-prediction-oryuo) | 🟡 Renfort |
| 3 | **Chikhen Dataset** | **236** | 6 (corps/tête/pattes) | [Roboflow](https://universe.roboflow.com/avitwins02/chikhen-ilszx) | 🟢 Complément |
| 4 | **Broiler Chicken Healthy and Sick** | **209** | 2 (Healthy/Sick) | [Roboflow](https://universe.roboflow.com/technicalresearch/broiler-chicken-healthy-and-sick) | 🟢 Complément |

---

## 3. Poultry Detection for Counter ⭐

| Caractéristique | Détail |
|----------------|--------|
| **Auteur** | Mohamed F. Abdelshafie |
| **Lien** | [Roboflow Universe](https://universe.roboflow.com/mohamed-f-abdelshafie/poultry-detection-for-counter) |
| **Volume** | **7 500 images** |
| **Format** | Object Detection (YOLO bounding boxes) |
| **Licence** | CC BY 4.0 |

### Classes (18)

| Classe | État | Mapping pour votre modèle |
|--------|------|--------------------------|
| `Healthy Broiler` | Sain ✅ | **healthy** |
| `Chicken` | Sain ✅ | **healthy** |
| `Bad cover` | Malade ❌ | **sick** |
| `Dirty collector` | Malade ❌ | **sick** |
| `Stressed chicken` | Malade ❌ | **sick** |
| `Lethargic chicken` | Malade ❌ | **sick** |
| `Sick leg` | Malade ❌ | **sick** |
| `Slipped tendons` | Malade ❌ | **sick** |
| `Unhealthy eye` | Malade ❌ | **sick** |
| `Bleeding` | Malade ❌ | **sick** |
| `Poop chicken` | ❌ Exclure | Fientes |
| `Dead chicken` | ❌ Exclure | Cas extrême |
| `.500 gm` | ❌ Exclure | Étiquette de poids |
| Autres (5) | À vérifier | Voir le dataset |

### Répartition estimée
- **Sain :** ~3 000+ images (Healthy Broiler + Chicken)
- **Malade :** ~3 000+ images (10 classes d'anomalies)
- **À exclure :** ~1 500 images

---

## 4. Disease Prediction

| Caractéristique | Détail |
|----------------|--------|
| **Auteur** | chicken-disease (Roboflow) |
| **Lien** | [Roboflow Universe](https://universe.roboflow.com/chicken-disease/disease-prediction-oryuo) |
| **Volume** | **1 200 images** |
| **Classes** | Normal, AbNormal |
| **Format** | Object Detection (YOLO) |
| **Rôle** | Renfort pour la classification binaire |

### Mapping
- `Normal` → **healthy** ✅
- `AbNormal` → **sick** ❌

---

## 5. Chikhen Dataset

| Caractéristique | Détail |
|----------------|--------|
| **Auteur** | Avitwins02 |
| **Lien** | [Roboflow Universe](https://universe.roboflow.com/avitwins02/chikhen-ilszx) |
| **Volume** | **236 images** |
| **Classes (6)** | Body anormal/normal, Feet anomaly/normal, Head anomaly/normal |
| **Format** | Object Detection (YOLO) |
| **Licence** | CC BY 4.0 |
| **Performance connue** | mAP@50 = 70.7%, Précision 92.0%, Rappel 67.8% |

### Mapping
- `Body normal`, `Feet normal`, `Head normal` → **healthy** ✅
- `Body anormal`, `Feet anomaly`, `Head anomaly` → **sick** ❌

### Points forts
- Structure idéale : découpage corps/tête/pattes
- Parfait pour un modèle multi-parties

---

## 6. Broiler Chicken Healthy and Sick

| Caractéristique | Détail |
|----------------|--------|
| **Auteur** | technicalresearch (Roboflow) |
| **Lien** | [Roboflow Universe](https://universe.roboflow.com/technicalresearch/broiler-chicken-healthy-and-sick) |
| **Volume** | **209 images** |
| **Classes** | Healthy, Sick |
| **Format** | Object Detection (YOLO) |
| **Rôle** | Renfort secondaire — classification binaire directe |

---

## 7. Comparatif et Analyse

### 7.1 Tableau Comparatif

| Critère | Poultry Detection ⭐ | Disease Prediction | Chikhen | Broiler H&S |
|---------|---------------------|-------------------|---------|-------------|
| **Volume** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐ |
| **Qualité annotations** | Excellente | Basique | Bonne | Basique |
| **Multi-classes** | ✅ 18 | ❌ 2 | ✅ 6 | ❌ 2 |
| **Mapping sain/malade** | ✅ 10+ classes utiles | ✅ Binaire | ✅ 3+3 | ✅ Binaire |
| **Licence** | CC BY 4.0 | ✅ | CC BY 4.0 | ✅ |

### 7.2 Classes disponibles pour votre classification cible

**Classe SAINE (`healthy`):**
- Poultry Detection → `Chicken`, `Healthy Broiler`
- Chikhen → `body normal`, `head normal`, `feet normal`
- Disease Prediction → `Normal`
- Broiler H&S → `Healthy`

**Classe MALADE (`sick`):**
- Poultry Detection → `Bad cover`, `Dirty collector`, `Stressed chicken`, `Lethargic chicken`, `Sick leg`, `Slipped tendons`, `Unhealthy eye`, `Bleeding`
- Chikhen → `body anormal`, `head anomaly`, `feet anomaly`
- Disease Prediction → `AbNormal`
- Broiler H&S → `Sick`

### 7.3 Recommandations

1. **Dataset principal :** `Poultry Detection for Counter` — 7 500 images, 18 classes
2. **Renfort binaire :** `Disease Prediction` — 1 200 images supplémentaires
3. **Détails anatomiques :** `Chikhen` — 236 images pour corps/tête/pattes
4. **Volume additionnel :** `Broiler H&S` — 209 images

> 💡 **Stratégie :** Fusionnez tous les datasets en deux dossiers `healthy/` et `sick/` avec un script de mapping des classes.

---

## 8. Guide de Téléchargement

### 8.1 Obtenir une clé API Roboflow

1. Créez un compte sur [Roboflow](https://roboflow.com/)
2. Allez dans **Settings → API Keys**
3. Copiez votre clé (ex: `rf_xxxxxxxxxxx`)

### 8.2 Installation

```bash
pip install roboflow
export ROBOFLOW_API_KEY="votre_clé_ici"
```

### 8.3 Téléchargement des 4 datasets

```python
from roboflow import Roboflow

rf = Roboflow(api_key="VOTRE_CLE_API")

# Dataset 1 : Poultry Detection for Counter (7 500 images)
project1 = rf.workspace("mohamed-f-abdelshafie").project("poultry-detection-for-counter")
version1 = project1.version(1)
version1.download("yolov8", location="datasets/01_poultry_detection_counter")

# Dataset 2 : Chikhen (236 images)
project2 = rf.workspace("avitwins02").project("chikhen-ilszx")
version2 = project2.version(1)
version2.download("yolov8", location="datasets/02_chikhen")

# Dataset 3 : Disease Prediction (1 200 images)
project3 = rf.workspace("chicken-disease").project("disease-prediction-oryuo")
version3 = project3.version(1)
version3.download("yolov8", location="datasets/03_disease_prediction")

# Dataset 4 : Broiler Chicken Healthy and Sick (209 images)
project4 = rf.workspace("technicalresearch").project("broiler-chicken-healthy-and-sick")
version4 = project4.version(1)
version4.download("yolov8", location="datasets/04_broiler_health")
```

### 8.4 Script automatisé

```bash
python3 scripts/download_all.py --roboflow-only
```

---

## 9. Structure de Données Recommandée

```
data-vik/
├── datasets/                         # Datasets bruts
│   ├── 01_poultry_detection_counter/ # Roboflow - 7 500 images
│   │   ├── train/
│   │   ├── valid/
│   │   └── test/
│   ├── 02_chikhen/                   # Roboflow - 236 images
│   ├── 03_disease_prediction/        # Roboflow - 1 200 images
│   └── 04_broiler_health/           # Roboflow - 209 images
├── merged/                           # Dataset fusionné (sain/malade)
│   ├── train/
│   │   ├── healthy/
│   │   └── sick/
│   ├── val/
│   │   ├── healthy/
│   │   └── sick/
│   └── test/
│       ├── healthy/
│       └── sick/
├── scripts/
│   ├── download_all.py               # Téléchargement
│   └── merge_datasets.py             # Fusion à créer
├── docs/
│   ├── 01_ROBOFLOW_POULTRY_DETECTION.md
│   ├── 02_ROBOFLOW_CHIKHEN.md
│   ├── 03_ROBOFLOW_DISEASE_PREDICTION.md
│   └── 04_ROBOFLOW_BROILER.md
├── info.txt                          # Note originale
└── rapport_complet.md                # Ce fichier
```

---

## 10. Considérations Éthiques et Légales

### 10.1 Licences

| Dataset | Licence | Utilisation Commerciale | Attribution |
|---------|---------|------------------------|-------------|
| Poultry Detection for Counter | CC BY 4.0 | ✅ Oui | ✅ Requise |
| Chikhen | CC BY 4.0 | ✅ Oui | ✅ Requise |
| Disease Prediction | Ouverte | ✅ Oui | ✅ Souhaitée |
| Broiler Chicken Healthy and Sick | Ouverte | ✅ Oui | ✅ Souhaitée |

### 10.2 Limitations

- **Volume :** ~9 145 images est un bon départ mais peut nécessiter de l'augmentation de données
- **Déséquilibre :** Vérifier la répartition sain/malade après fusion
- **Généralisation :** Les modèles Roboflow sont souvent collectés dans des conditions spécifiques
- **Confirmation vétérinaire :** Ces modèles sont des aides au diagnostic, pas un remplacement

### 10.3 Prochaines étapes recommandées

1. Télécharger les 4 datasets avec votre clé API Roboflow
2. Créer un script de mapping des classes → `healthy` / `sick`
3. Équilibrer les classes (data augmentation)
4. Entraîner un modèle YOLOv8 ou MobileNetV2

---

## Annexes

### Annexe A : Modèles recommandés

| Modèle | Taille | Précision | Adapté Mobile |
|--------|--------|-----------|---------------|
| YOLOv8n | 6 MB | ~92% mAP | ✅ |
| YOLOv8s | 22 MB | ~95% mAP | ✅ |
| MobileNetV2 | 14 MB | ~95% | ✅ |
| EfficientNet-B0 | 20 MB | ~97% | ✅ |

### Annexe B : Métriques d'évaluation

- Accuracy, Precision, Recall, F1-Score
- Matrice de confusion
- AUC-ROC
- mAP@50 (pour détection)

---

*Rapport généré le 18 juillet 2026 — version nettoyée (fèces exclus).*
