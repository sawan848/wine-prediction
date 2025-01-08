import setuptools
from typing import List
HYPHEN_E_DOT='-e .'

with open('README.MD',"r", encoding="utf-8") as f:
    long_description=f.read()
    

__version__="0.0.0"


setuptools.setup(
    name='WinePrediction',
    version=__version__,
    author='Sawan Kumar',
    author_email="ksawan802@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
   
) 

