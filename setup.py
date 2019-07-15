# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_ = f.read()

setup(
    name='package',  # FIXME
    version='0.1.0',
    description='An easy to use project template for Python',  # FIXME
    long_description=readme,
    author='Mario Bonito', 
    author_email='mario@beelabs.ca',
    url='https://github.com/masterbee/python-template',  # FIXME
    install_requires=[
        # FIXME
    ],
    license=license_,
    packages=find_packages(exclude=('tests', 'docs'))
)
