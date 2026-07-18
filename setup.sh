#!/usr/bin/env bash
# ============================================
# Script d'installation - Détection Maladies Aviaires
# Utilisation : bash setup.sh
# ============================================

set -e

echo ""
echo "  ╔══════════════════════════════════════════════╗"
echo "  ║     🐔 Installation du Projet Aviaire        ║"
echo "  ╚══════════════════════════════════════════════╝"
echo ""

# Vérifier Python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "  ❌ Python introuvable. Installez Python 3.12+ :"
    echo "     https://www.python.org/downloads/"
    exit 1
fi

echo "  ✅ Python trouvé : $($PYTHON --version)"
echo ""

# Vérifier pip
if ! $PYTHON -m pip --version &> /dev/null; then
    echo "  ❌ pip introuvable."
    exit 1
fi
echo "  ✅ pip trouvé"
echo ""

# Créer le venv
echo "  ▶ Création de l'environnement virtuel..."
$PYTHON -m venv venv
echo "  ✅ venv créé"
echo ""

# Activer le venv et installer les dépendances
echo "  ▶ Installation des dépendances..."
source venv/bin/activate
$PYTHON -m pip install --upgrade pip --quiet
$PYTHON -m pip install -r requirements.txt
echo "  ✅ Dépendances installées"
echo ""

# Configurer .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo "  ▶ Fichier .env créé depuis .env.example"
    echo "  ⚠️  OUVREZ .env et ajoutez votre clé ROBOFLOW_API_KEY !"
    echo "     Obtenez-la sur : https://app.roboflow.com/settings/api"
    echo ""
else
    echo "  ✅ Fichier .env déjà existant"
fi

# Rendre le script exécutable
chmod +x scripts/download_all.py 2>/dev/null || true

echo "  ╔══════════════════════════════════════════════╗"
echo "  ║     ✅ Installation terminée !               ║"
echo "  ╚══════════════════════════════════════════════╝"
echo ""
echo "  Prochaine étape :"
echo "    1. Activez le venv : source venv/bin/activate"
echo "    2. Téléchargez les datasets :"
echo "       python scripts/download_all.py --roboflow-only"
echo ""
