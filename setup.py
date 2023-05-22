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
       'blinker==1.6.2',
       'certifi==2023.5.7',
       'charset-normalizer==3.1.0',
       'click==8.1.3',
       'Flask==2.3.2',
       'idna==3.4',
       'iniconfig==2.0.0',
       'itsdangerous==2.1.2',
       'Jinja2==3.1.2',
       'MarkupSafe==2.1.2',
       'packaging==23.1',
       'pluggy==1.0.0',
       'pytest==7.3.1',
       'requests==2.30.0',
       'urllib3==2.0.2',
       'Werkzeug==2.3.3'
    ]
)
