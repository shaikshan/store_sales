from setuptools import setup,find_packages
from typing import List

#Declare variables for setup functions
PROJECT_NAME ='store-sales'
VERSION = '0.0.3'
AUTHOR = 'Roshan Zameer'
DESCRIPTION = "This is a Machine Learning based project"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
        

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires = get_requirements_list()
    )