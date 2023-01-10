import os

DB_ROOT_DIR = os.path.join(os.getcwd(), "data")
CONFIG_ROOT_DIR = os.path.join(os.getcwd(), "config")

def get_config_path(filename: str) -> str:
    return os.path.join(CONFIG_ROOT_DIR, filename)
