# Disease Prediction

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

## Téléchargement (version dynamique)
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("chicken-disease").project("disease-prediction-oryuo")
# Utiliser la dernière version disponible (détection automatique)
latest = project.versions()[-1]
version = project.version(latest if not hasattr(latest, 'version') else latest.version)
version.download("yolov8", overwrite=True)
```

> 💡 Le script `download_all.py` gère automatiquement la détection de version.
> Pour un téléchargement simple, utilisez : `python scripts/download_all.py --roboflow-only`
