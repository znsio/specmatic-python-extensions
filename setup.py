import os

from setuptools import setup, find_packages
import urllib.request


def download_specmatic_jar(version):
    file_url = f'https://github.com/znsio/specmatic/releases/download/{version}/specmatic.jar'
    file_path = 'specmatic_python/specmatic/specmatic.jar'
    print(f"Downloading specmatic jar from: {file_url}")
    urllib.request.urlretrieve(file_url, file_path)


def get_version():
    version = {}
    with open(os.path.join('specmatic_python', 'version.py')) as file:
        exec(file.read(), version)
    return version


specmatic_python_version = get_version()

download_specmatic_jar(specmatic_python_version['__version__'])

setup(
    name='specmatic-python',
    version=specmatic_python_version['__version__'],
    description='A Python module for using the Specmatic Library.',
    author='Specmatic Builders',
    author_email='info@specmatic.in',
    url='https://github.com/znsio/specmatic-python-extensions',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'blinker==1.6.2',
        'click==8.1.3',
        'Flask==2.3.2',
        'iniconfig==2.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.2',
        'packaging==23.1',
        'pluggy==1.0.0',
        'pytest==7.3.1',
        'Werkzeug==2.3.3'
    ]
)
