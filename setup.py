from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "mpass",
    version = "0.0.1",
    packages = find_packages(),
    scripts = ['scripts/mpass'],
    
    author = "Ben Pringle",
    author_email = "ben.pringle@gmail.com",
    description = "Hash-based password management",
    license = "Apache License (2.0)",
)
