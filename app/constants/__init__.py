import os
from pathlib import Path

ROOT_DIR = os.path.abspath(Path(os.getcwd()))
CONFIG_PATH = f"{ROOT_DIR}/.config"
GALLERY_IMG_SIZE = (100,100)
NUM_MOST_FREQ_COLORS = 25