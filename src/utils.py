import os
from pathlib import Path


def get_project_root() -> str:
    return os.path.dirname(Path(__file__).parent)
