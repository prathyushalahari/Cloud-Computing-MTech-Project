from typing import List
from setuptools import setup, find_packages

HYPHEN_E_DOT = '-e.'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(

    name='cloud_project',
    version='0.0.1',
    author='Prathyusha Lahari',
    author_email='m.prathyushalahari@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
