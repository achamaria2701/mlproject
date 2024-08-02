from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

#this function will return the requiremnts in a list form
def get_requirements(file_path:str)->List[str]: 
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  #this statement read line with '\n' after every line. We need to remove that
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='ac',
    author_email='ankitchamaria1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)