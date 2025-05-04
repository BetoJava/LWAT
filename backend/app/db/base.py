from pathlib import Path
from tinydb import TinyDB

# Configuration TinyDB
BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "data" / "db.json"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

db = TinyDB(DB_PATH)
users_table: TinyDB.table = db.table("users")
