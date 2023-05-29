import os
from pathlib import Path

from setuptools import setup, find_packages
import urllib.request


def download_specmatic_jar(version):
    file_url = f'https://github.com/znsio/specmatic/releases/download/{version}/specmatic.jar'
    file_path = 'specmatic/core/specmatic.jar'
    print(f"Downloading core jar from: {file_url}")
    urllib.request.urlretrieve(file_url, file_path)


def get_version():
    version = {}
    with open(os.path.join('specmatic', 'version.py')) as file:
        exec(file.read(), version)
    return version


version = get_version()

download_specmatic_jar(version['__specmatic_version__'])

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='specmatic',
    version=version['__version__'],
    description='A Python module for using the Specmatic Library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Specmatic Builders',
    author_email='info@core.in',
    url='https://github.com/znsio/specmatic-python-extensions',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
       'pytest==7.3.1',
       'requests>=2.0.0',
       'Werkzeug==2.3.3',
       'uvicorn>=0.18.0'
    ]
)
