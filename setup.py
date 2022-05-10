from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in traval_app/__init__.py
from traval_app import __version__ as version

setup(
	name="traval_app",
	version=version,
	description="traval app managment",
	author="efeone",
	author_email="jmasheerak678@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
