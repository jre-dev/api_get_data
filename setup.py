from setuptools import setup, find_packages

from api_get_data.main import __version__

setup(
    name='API_get_data',
    version=__version__,
    author='J K R',
    packages=find_packages(),
)
