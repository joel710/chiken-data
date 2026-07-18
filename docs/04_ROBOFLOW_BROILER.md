# Broiler Chicken Healthy and Sick

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

## Téléchargement (version dynamique)
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("technicalresearch").project("broiler-chicken-healthy-and-sick")
# Utiliser la dernière version disponible (détection automatique)
latest = project.versions()[-1]
version = project.version(latest if not hasattr(latest, 'version') else latest.version)
version.download("yolov8", overwrite=True)
```

> 💡 Le script `download_all.py` gère automatiquement la détection de version.
> Pour un téléchargement simple, utilisez : `python scripts/download_all.py --roboflow-only`
