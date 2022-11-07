from setuptools import setup
from setuptools import find_packages

setup(
    name='toolkit',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'boto3', 'click' 
    ],
    entry_points={'console_scripts': ['toolkit=toolkit.cli:entry_point']}
)

