# Chikhen Dataset

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

## Téléchargement (version dynamique)
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("avitwins02").project("chikhen-ilszx")
# Utiliser la dernière version disponible (détection automatique)
latest = project.versions()[-1]
version = project.version(latest if not hasattr(latest, 'version') else latest.version)
version.download("yolov8", overwrite=True)
```

> 💡 Le script `download_all.py` gère automatiquement la détection de version.
> Pour un téléchargement simple, utilisez : `python scripts/download_all.py --roboflow-only`
