import os
from setuptools import setup, find_packages
import sys

sys.path.append(os.path.dirname(__file__))

import DiffusionConformer

with open("README.md") as f:
    readme = f.read()

with open("LICENSE.md") as f:
    license = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

pkgs = find_packages(exclude=("example", "checkpoints", "media", "output"))

setup(
    name="DiffusionConformer",
    version=DiffusionConformer.__version__,  # TODO: switch to versioneer.get_version() or alternate method
    description="Diffusion conformer generation",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="David C. Williams and Neil Inala",
    license=license,
    packages=pkgs,
    python_requires="==3.9.*",
    install_requires=install_requires,
)
