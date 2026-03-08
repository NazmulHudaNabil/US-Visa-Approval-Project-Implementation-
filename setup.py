from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Nabil",
    author_email="nabil648777@gmail.com",
    packages=find_packages(include=["us_visa", "us_visa.*"]),
)