import setuptools
from typing import List
HYPHEN_E_DOT='-e .'

with open('README.MD',"r", encoding="utf-8") as f:
    long_description=f.read()
    

__version__="0.0.0"
AUTHOR_USER_NAME="sawan848"
REPO_NAME="wine-prediction"

setuptools.setup(
    name='WinePrediction',
    version=__version__,
    author='Sawan Kumar',
    author_email="ksawan802@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
   
) 

