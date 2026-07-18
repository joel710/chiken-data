# Poultry Detection for Counter ⭐

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

## Téléchargement (version dynamique)
```python
from roboflow import Roboflow
rf = Roboflow(api_key="VOTRE_CLE")
project = rf.workspace("mohamed-f-abdelshafie").project("poultry-detection-for-counter")
# Utiliser la dernière version disponible (détection automatique)
latest = project.versions()[-1]
version = project.version(latest if not hasattr(latest, 'version') else latest.version)
version.download("yolov8", overwrite=True)
```

> 💡 Le script `download_all.py` gère automatiquement la détection de version.
> Pour un téléchargement simple, utilisez : `python scripts/download_all.py --roboflow-only`
