# Setup
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

# Run backend
cd app
uvicorn main:app --reload

# Architecture & Bonnes pratiques
- app/api/ : contient uniquement les routers (préfixés /api/v1) et la traduction des erreurs métier en HTTPException.
- app/services/ : toute la logique métier complexe (vérifications, règles, notifications, etc.).
- app/db/ : configuration et accès brut à la base (TinyDB).
- app/schemas/ : modèles Pydantic pour la validation et la sérialisation.
- app/core/ : configuration générale de l’application (variables d’environnement).