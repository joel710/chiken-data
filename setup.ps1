# ============================================
# Script d'installation - Détection Maladies Aviaires
# Utilisation : .\setup.ps1
# ============================================

Write-Host ""
Write-Host "  ╔══════════════════════════════════════════════╗"
Write-Host "  ║     🐔 Installation du Projet Aviaire        ║"
Write-Host "  ╚══════════════════════════════════════════════╝"
Write-Host ""

# Vérifier Python
$pythonCmd = $null
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        $pythonCmd = "python"
        Write-Host "  ✅ Python trouvé : $pythonVersion"
    }
} catch {}
if (-not $pythonCmd) {
    try {
        $pythonVersion = python3 --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $pythonCmd = "python3"
            Write-Host "  ✅ Python trouvé : $pythonVersion"
        }
    } catch {}
}
if (-not $pythonCmd) {
    Write-Host "  ❌ Python introuvable. Installez Python 3.12+ :"
    Write-Host "     https://www.python.org/downloads/"
    exit 1
}

Write-Host ""

# Vérifier pip
try {
    & $pythonCmd -m pip --version > $null 2>&1
    Write-Host "  ✅ pip trouvé"
} catch {
    Write-Host "  ❌ pip introuvable."
    exit 1
}

Write-Host ""

# Créer le venv
Write-Host "  ▶ Création de l'environnement virtuel..."
& $pythonCmd -m venv venv
Write-Host "  ✅ venv créé"
Write-Host ""

# Installer les dépendances
Write-Host "  ▶ Installation des dépendances..."
& .\venv\Scripts\pip install --upgrade pip --quiet
& .\venv\Scripts\pip install -r requirements.txt
Write-Host "  ✅ Dépendances installées"
Write-Host ""

# Configurer .env
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "  ▶ Fichier .env créé depuis .env.example"
    Write-Host "  ⚠️  OUVREZ .env et ajoutez votre clé ROBOFLOW_API_KEY !"
    Write-Host "     Obtenez-la sur : https://app.roboflow.com/settings/api"
    Write-Host ""
} else {
    Write-Host "  ✅ Fichier .env déjà existant"
}

Write-Host "  ╔══════════════════════════════════════════════╗"
Write-Host "  ║     ✅ Installation terminée !               ║"
Write-Host "  ╚══════════════════════════════════════════════╝"
Write-Host ""
Write-Host "  Prochaine étape :"
Write-Host "    1. Activez le venv : .\venv\Scripts\Activate.ps1"
Write-Host "    2. Téléchargez les datasets :"
Write-Host "       python scripts/download_all.py --roboflow-only"
Write-Host ""

# Si l'exécution est bloquée, lancer PowerShell en admin et faire :
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
