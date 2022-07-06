from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="src",
    version="0.0.1",
    author="chandra",
    description="A small package for dvc ml pipeline demo",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url="https://github.com/chandra-general/ML-AIOPS.git",
    author_email="chandra.tiyyagura@gmail.com",
    packages=["src"],
    License="GNU",
    python_branch=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
