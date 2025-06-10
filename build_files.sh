#!/bin/bash
echo "BUILD START"

export PATH="/vercel/.local/bin:/python312/bin:/python39/bin:$PATH"


# Afficher l'environnement
echo "Python version:"
python3 --version
echo "Pip version:"
pip --version
echo "Node version:"
node --version
echo "NPM version:"
npm --version

# Vérifier que les dépendances sont installées
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Vérifier l'installation de django-environ
echo "Checking django-environ..."
if ! python3 -c "import environ" &>/dev/null; then
  echo "Installing django-environ..."
  python3 -m pip install django-environ
fi 

# Générer les fichiers CSS Tailwind
echo "Building Tailwind CSS..."
cd theme/static_src
npm install
npm run build
cd ../..

# Collecter les fichiers statiques
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Forcer l'installation de whitenoise spécifiquement
echo "Installation forcée de whitenoise..."
python3 -m pip install whitenoise

echo "BUILD END"