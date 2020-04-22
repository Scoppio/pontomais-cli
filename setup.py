from pontomais import __version__
from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()

setup(
    name="pontomais cli",
    version=__version__,
    description='Command line client and utilities for Pontomais',
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Utilities :: CLI",
        "Framework :: Click",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='cli pontomais',
    author="Lucas S. Coppio",
    author_email='lucas@strider.ag',
    url='https://github.com/Scoppio/pontomais-cli',
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    zip_safe=True,
    install_requires=requirements,
    entry_points='''
        [console_scripts]
            ptm = pontomais.__main__:cli
            ptm-configure = pontomais.__main__:login
            ''',
)