from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="common_services",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Adam Sequeira",
    author_email="adamsequeira@outlook.com",
    description="common data services",
    long_description="for common data services",
    long_description_content_type="text/markdown",
    url="https://github.com/addybrown/common_services",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
