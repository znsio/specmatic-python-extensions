from pathlib import Path

from specmatic.build_utils import download_specmatic_jar, get_version
from specmatic.utils import get_project_root


def download_specmatic_jar_if_does_not_exist():
    specmatic_jar_file = Path(get_project_root() + '/specmatic/core/specmatic.jar')
    if not specmatic_jar_file.is_file():
        version = get_version(get_project_root() + '/specmatic/version.py')
        download_specmatic_jar(version['__specmatic_version__'])
