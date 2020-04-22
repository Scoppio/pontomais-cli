from setuptools import setup, find_packages
from protector_cli import __version__, project_name, __author__
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().split()

setup(
    name=project_name,
    version=__version__,
    description='Command Line Client for Protector',
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Utilities :: CLI",
        "Framework :: Click",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='cli protector admin',
    author="Lucas S. Coppio",
    author_email='lucas@strider.ag',
    url='https://github.com/striderag/protector_cli/wiki',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points='''
        [console_scripts]
            stp = protector_cli.ProtectorCLI:cli
            stp-config = protector_cli.ProtectorCLI:config
            stp-pip = protector_cli.PluginController:cli
            stp-pip-config = protector_cli.PluginController:config_updater
            ''',
)

with open("version.json", "w") as e:
    version_file = {"version": __version__,
                    "project": project_name, "author": __author__}
    e.write(str(version_file).replace("'", '"'))
