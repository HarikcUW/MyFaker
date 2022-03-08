
from setuptools import find_packages
from setuptools import setup

#with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()

setup(
    name="myfaker",
    author="Hari Kishor Chintada",
    author_email="harikc@uw.edu",
    description="Fake data generator",
    long_description="Fake data generator",
    long_description_content_type="text/markdown",
    url="https://github.com/harikcUW/myfaker/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages= find_packages(),
    python_requires=">=3.0",
    #install_requires=['pandas', 'rsts']
)
