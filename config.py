import json
import os

CONFIG_DIR = "user_config"
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
COORDS_PATH = os.path.join(CONFIG_DIR, "coords_config.json")

DEFAULT_KEYWORDS = [{"keyword": "想要的扣1", "response": "111"}]
DEFAULT_COORDS = {}

os.makedirs(CONFIG_DIR, exist_ok=True)

def load_json(path, default):
    if not os.path.exists(path):
        save_json(path, default)
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_keywords():
    return load_json(CONFIG_PATH, DEFAULT_KEYWORDS)

def load_coords():
    return load_json(COORDS_PATH, DEFAULT_COORDS)

def save_keywords(keywords):
    save_json(CONFIG_PATH, keywords)

def save_coords(coords):
    save_json(COORDS_PATH, coords)
