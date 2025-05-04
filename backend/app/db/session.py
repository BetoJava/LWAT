from tinydb import TinyDB, Query
from pathlib import Path
from ..core.config import config

# Assure-toi que le dossier existe
config.TINYDB_PATH.parent.mkdir(exist_ok=True, parents=True)

db = TinyDB(config.TINYDB_PATH)  
