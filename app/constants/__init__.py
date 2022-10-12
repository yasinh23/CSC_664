import os
from app.backend.helpers.Config import Config
from pathlib import Path

ROOT_DIR = os.path.abspath(Path(os.getcwd()))
CONFIG_FILENAME = '.config'
CONFIG_PATH = f"{ROOT_DIR}/{CONFIG_FILENAME}"
CONFIG_FILE = Config(CONFIG_PATH)

# Config settings required for program to run correctly
REQUIRED_CONFIGS = ['gallery_dir']

GALLERY_CARD_SIZE = 150
GALLERY_ROWS = 3
GALLERY_COL = 3
GALLERY_IMG_SIZE = (100,100)

MONTH_DICT = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}