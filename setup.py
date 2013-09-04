from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "mpass",
    version = "0.0.2",
    packages = find_packages(),
    scripts = ['scripts/mpass'],

    url = "https://github.com/Pringley/mpass-python",
    
    author = "Ben Pringle",
    author_email = "ben.pringle@gmail.com",
    description = "Hash-based password management",
    license = "Apache License (2.0)",
)
