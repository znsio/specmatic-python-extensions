import os
from pathlib import Path


def get_project_root() -> str:
    return os.path.dirname(Path(__file__).parent)


def get_junit_report_dir_path() -> str:
    return get_project_root() + "/junit_report"


def get_junit_report_file_path() -> str:
    return get_junit_report_dir_path() + "/TEST-junit-jupiter.xml"
