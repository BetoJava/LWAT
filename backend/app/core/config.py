from pydantic import BaseSettings
from pathlib import Path
import dotenv

dotenv_path = Path(__file__).parent.parent.parent / ".env"
dotenv.load_dotenv(dotenv_path)

class Settings(BaseSettings):
    # Chemin vers la base TinyDB
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    TINYDB_PATH: Path = BASE_DIR / "data" / "db.json"
    

config = Settings()
