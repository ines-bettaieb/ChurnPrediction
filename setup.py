from setuptools import setup, find_packages
from typing import List


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="Churn Prediction",
    version="0.1.0",
    author="Ines Bettaieb",
    description="A churn prediction project using Azure and machine learning pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)