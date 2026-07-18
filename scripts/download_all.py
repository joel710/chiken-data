#!/usr/bin/env python3
"""
Script de téléchargement des datasets de détection de maladies aviaires.

Seulement les datasets d'IMAGES CORPORELLES (volaille sur la photo).
✅ Exclus : fientes, fèces, lésions, datasets Kaggle, Zenodo, Mendeley.

Utilisation :
    python3 scripts/download_all.py --list               # Lister les datasets
    python3 scripts/download_all.py --roboflow-only      # Télécharger depuis Roboflow
    python3 scripts/download_all.py --docs-only          # Générer la documentation

Configuration :
    Copier .env.example -> .env et remplir ROBOFLOW_API_KEY
    Ou exporter la variable : export ROBOFLOW_API_KEY='votre_clé'
"""

import os
import json
import glob
import argparse
import shutil
from pathlib import Path

# Charger les variables du fichier .env s'il existe
from dotenv import load_dotenv
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
DOCS_DIR = BASE_DIR / "docs"

for d in [DATASETS_DIR, DOCS_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def print_header(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_step(msg):
    print(f"  ▶ {msg}")


def print_ok(msg):
    print(f"  ✅ {msg}")


def print_warn(msg):
    print(f"  ⚠️  {msg}")


def print_err(msg):
    print(f"  ❌ {msg}")


# =============================================================================
# DATASETS ROBOFLOW (corps de volaille uniquement)
# =============================================================================
ROBOFLOW_DATASETS = [
    {
        "id": "01_poultry_detection_counter",
        "workspace": "mohamed-f-abdelshafie",
        "project": "poultry-detection-for-counter",
        "name": "Poultry Detection for Counter ⭐",
        "classes": 18,
        "images": 7500,
        "version": "latest",
        "type": "Corps entier + détails tête/pattes/plumage",
    },
    {
        "id": "02_chikhen",
        "workspace": "avitwins02",
        "project": "chikhen-ilszx",
        "name": "Chikhen Dataset",
        "classes": 6,
        "images": 236,
        "version": "latest",
        "type": "Corps / Tête / Pattes (normal vs anormal)",
    },
    {
        "id": "03_disease_prediction",
        "workspace": "chicken-disease",
        "project": "disease-prediction-oryuo",
        "name": "Disease Prediction",
        "classes": 2,
        "images": 1200,
        "version": "latest",
        "type": "Corps entier (Normal vs AbNormal)",
    },
    {
        "id": "04_broiler_health",
        "workspace": "technicalresearch",
        "project": "broiler-chicken-healthy-and-sick",
        "name": "Broiler Chicken Healthy and Sick",
        "classes": 2,
        "images": 209,
        "version": "latest",
        "type": "Corps entier (Healthy vs Sick)",
    },
]


def download_roboflow():
    """Télécharge les 4 datasets Roboflow d'images corporelles."""
    print_header("TÉLÉCHARGEMENT DES DATASETS ROBOFLOW")
    print("  4 datasets d'images corporelles de volailles")
    print("  ✅ Fèces, fientes, lésions EXCLUS")
    print()

    api_key = os.environ.get("ROBOFLOW_API_KEY", "")
    base_url = "https://universe.roboflow.com"

    if not api_key:
        print_warn("ROBOFLOW_API_KEY non définie.")
        print_step("Configurez votre clé dans le fichier .env :")
        print_step("  1. Copiez .env.example -> .env")
        print_step("  2. Ouvrez .env et collez votre clé Roboflow")
        print_step("     ROBOFLOW_API_KEY='rf_votre_clé'")
        print_step("  3. Obtenez votre clé : https://app.roboflow.com/settings/api")
        print()

    try:
        from roboflow import Roboflow
        rf = Roboflow(api_key=api_key) if api_key else None
    except ImportError:
        print_err("Package manquant : pip install roboflow")
        rf = None

    for ds in ROBOFLOW_DATASETS:
        print(f"\n  [{ds['workspace']}/{ds['project']}]")
        print(f"    {ds['name']}")
        print(f"    {ds['images']} images, {ds['classes']} classes")
        print(f"    Type : {ds['type']}")

        dest_dir = DATASETS_DIR / ds['id']
        # Nettoyage pour éviter les résidus des téléchargements précédents
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Sauvegarder les infos
        info = {
            "name": ds["name"],
            "url": f"{base_url}/{ds['workspace']}/{ds['project']}",
            "images": ds["images"],
            "classes": ds["classes"],
            "type": ds["type"],
            "workspace": ds["workspace"],
            "project": ds["project"],
            "version": ds["version"],
        }
        with open(dest_dir / "dataset_info.json", "w") as f:
            json.dump(info, f, indent=2)
        print_ok("Informations sauvegardées")

        if not api_key or not rf:
            print_warn("Téléchargement manuel :")
            print(f"       {base_url}/{ds['workspace']}/{ds['project']}")
            continue

        try:
            print_step("Téléchargement via API Roboflow...")
            project = rf.workspace(ds["workspace"]).project(ds["project"])
            
            # Détection de la dernière version si "latest"
            if ds["version"] == "latest":
                versions = project.versions()
                if not versions:
                    print_err("Aucune version trouvée pour ce projet !")
                    print_step(f"Téléchargement manuel : {base_url}/{ds['workspace']}/{ds['project']}")
                    continue
                latest_version = versions[-1].version if hasattr(versions[-1], 'version') else versions[-1]
                print_step(f"Dernière version détectée : {latest_version}")
            else:
                latest_version = ds["version"]
            
            version = project.version(latest_version)
            result = version.download("yolov8", location=str(dest_dir), overwrite=True)
            print_ok(f"Téléchargé dans {dest_dir}")
            
            # Vérifier que les fichiers sont bien présents
            files = glob.glob(f"{dest_dir}/**/*.*", recursive=True)
            if files:
                image_count = sum(1 for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png')))
                print_ok(f"{len(files)} fichiers trouvés ({image_count} images)")
            else:
                print_warn("Aucun fichier trouvé dans le dossier de destination")
                print_warn("Vérifiez que l'export s'est terminé correctement")
                
        except Exception as e:
            print_err(f"Erreur : {e}")
            print_step(f"Téléchargement manuel : {base_url}/{ds['workspace']}/{ds['project']}")

    return True


# =============================================================================
# Documentation (4 datasets corporels uniquement)
# =============================================================================
def generate_docs():
    """Génère la documentation des 4 datasets corporels."""
    print_header("DOCUMENTATION DES DATASETS")

    docs_dir = DOCS_DIR
    docs_dir.mkdir(parents=True, exist_ok=True)

    docs = {
        "01_ROBOFLOW_POULTRY_DETECTION.md": f"""# Poultry Detection for Counter ⭐

## Référence
- **Auteur :** Mohamed F. Abdelshafie
- **Lien :** https://universe.roboflow.com/mohamed-f-abdelshafie/poultry-detection-for-counter
- **Licence :** CC BY 4.0
- **Volume :** 7 500 images
- **Classes :** 18

## Classes et mapping

| Classe | Mapping | Description |
|--------|---------|-------------|
| Chicken | healthy ✅ | Volaille normale |
| Healthy Broiler | healthy ✅ | Poulet sain |
| Bad cover | sick ❌ | Mauvais plumage |
| Dirty collector | sick ❌ | Collecteur sale |
| Stressed chicken | sick ❌ | Stressé |
| Lethargic chicken | sick ❌ | Léthargique |
| Sick leg | sick ❌ | Patte malade |
| Slipped tendons | sick ❌ | Tendons déplacés |
| Unhealthy eye | sick ❌ | Œil malade |
| Bleeding | sick ❌ | Saignement |

## Classes à exclure
- Poop chicken (fientes)
- Dead chicken (cas extrême)
- .500 gm (poids)

## Téléchargement
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("mohamed-f-abdelshafie").project("poultry-detection-for-counter")
version = project.version(1)
version.download("yolov8")
```
""",
        "02_ROBOFLOW_CHIKHEN.md": f"""# Chikhen Dataset

## Référence
- **Auteur :** Avitwins02
- **Lien :** https://universe.roboflow.com/avitwins02/chikhen-ilszx
- **Licence :** CC BY 4.0
- **Volume :** 236 images
- **Classes :** 6

## Classes et mapping

| Classe | Mapping | Description |
|--------|---------|-------------|
| Body normal | healthy ✅ | Corps normal |
| Body anormal | sick ❌ | Corps anormal |
| Feet normal | healthy ✅ | Pattes normales |
| Feet anomaly | sick ❌ | Pattes anormales |
| Head normal | healthy ✅ | Tête normale |
| Head anomaly | sick ❌ | Tête anormale |

## Performance connue
- mAP@50: 70.7%
- Précision: 92.0%
- Rappel: 67.8%

## Téléchargement
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("avitwins02").project("chikhen-ilszx")
version = project.version(1)
version.download("yolov8")
```
""",
        "03_ROBOFLOW_DISEASE_PREDICTION.md": f"""# Disease Prediction

## Référence
- **Auteur :** chicken-disease (Roboflow)
- **Lien :** https://universe.roboflow.com/chicken-disease/disease-prediction-oryuo
- **Volume :** 1 200 images
- **Classes :** 2

## Classes et mapping

| Classe | Mapping | Description |
|--------|---------|-------------|
| Normal | healthy ✅ | Volaille saine |
| AbNormal | sick ❌ | Volaille anormale |

## Téléchargement
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("chicken-disease").project("disease-prediction-oryuo")
version = project.version(1)
version.download("yolov8")
```
""",
        "04_ROBOFLOW_BROILER.md": f"""# Broiler Chicken Healthy and Sick

## Référence
- **Auteur :** technicalresearch (Roboflow)
- **Lien :** https://universe.roboflow.com/technicalresearch/broiler-chicken-healthy-and-sick
- **Volume :** 209 images
- **Classes :** 2

## Classes et mapping

| Classe | Mapping | Description |
|--------|---------|-------------|
| Healthy | healthy ✅ | Poulet sain |
| Sick | sick ❌ | Poulet malade |

## Téléchargement
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("technicalresearch").project("broiler-chicken-healthy-and-sick")
version = project.version(1)
version.download("yolov8")
```
""",
    }

    for filename, content in docs.items():
        filepath = docs_dir / filename
        with open(filepath, "w") as f:
            f.write(content.strip() + "\n")
        print_ok(f"Documentation : {filename}")

    return True


# =============================================================================
# Liste
# =============================================================================
def list_datasets():
    """Liste les datasets corporels disponibles."""
    print_header("DATASETS DISPONIBLES (images corporelles uniquement)")
    print()
    print("  ┌──────┬──────────────────────────────────────────┬──────────┬────────┬──────────┐")
    print("  │  #   │ Dataset                                  │ Images   │Classes │ Type     │")
    print("  ├──────┼──────────────────────────────────────────┼──────────┼────────┼──────────┤")
    print("  │  1   │ Poultry Detection for Counter ⭐        │ 7 500    │  18    │ Corps    │")
    print("  │  2   │ Disease Prediction                       │ 1 200    │   2    │ Corps    │")
    print("  │  3   │ Chikhen                                  │ 236      │   6    │ Corps/tête/pattes │")
    print("  │  4   │ Broiler Chicken Healthy and Sick         │ 209      │   2    │ Corps    │")
    print("  └──────┴──────────────────────────────────────────┴──────────┴────────┴──────────┘")
    print()
    print(f"  📦 Volume total : ~9 145 images (annoncés)")
    print(f"  ⚠️  Le téléchargement via API peut retourner un sous-ensemble (∼2 300 images)")
    print(f"  ✅ Tous les datasets de fientes, fèces, lésions ont été EXCLUS")
    print()


# =============================================================================
# Main
# =============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Téléchargeur de datasets aviaires (corps uniquement)"
    )
    parser.add_argument("--list", action="store_true", help="Lister les datasets")
    parser.add_argument("--roboflow-only", action="store_true", help="Télécharger depuis Roboflow")
    parser.add_argument("--docs-only", action="store_true", help="Générer la documentation")
    parser.add_argument("--all", action="store_true", help="Tout faire")

    args = parser.parse_args()

    if args.list:
        list_datasets()
        return

    do_all = args.all or not (args.roboflow_only or args.docs_only)

    print_header("TÉLÉCHARGEUR DATASETS AVIAIRES — CORPS UNIQUEMENT")
    print("  ✅ Datasets de fientes, fèces, lésions EXCLUS")
    print()

    if do_all or args.docs_only:
        generate_docs()

    if do_all or args.roboflow_only:
        download_roboflow()

    print_header("RÉSUMÉ")
    print()
    print(f"  📄 Rapport  : {BASE_DIR / 'rapport_complet.md'}")
    print(f"  📁 Docs     : {DOCS_DIR}/")
    print(f"  📂 Datasets : {DATASETS_DIR}/")
    print()
    print("  Pour télécharger :")
    print("    1. Copiez .env.example -> .env et ajoutez votre clé")
    print("    2. python3 scripts/download_all.py --roboflow-only")
    print()


if __name__ == "__main__":
    main()
