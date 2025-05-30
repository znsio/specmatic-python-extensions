import urllib.request

from specmatic.utils import get_project_root


def download_specmatic_jar(version):
    file_url = f"https://github.com/specmatic/specmatic/releases/download/{version}/specmatic.jar"
    file_path = get_project_root() + "/specmatic/core/specmatic.jar"
    print(f"Downloading specmatic jar from: {file_url}")
    urllib.request.urlretrieve(file_url, file_path)


def get_version(version_py_path):
    version = {}
    with open(version_py_path) as file:
        exec(file.read(), version)
    return version
