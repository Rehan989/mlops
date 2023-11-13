from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(filename: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(filename, "r") as file1:
        requirements = file1.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
    
setup(
    name='mlproject',
    version="0.0.1",
    author="Rehan",
    author_email="rehanmakrani727@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)