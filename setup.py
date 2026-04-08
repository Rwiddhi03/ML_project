from setuptools import find_packages , setup
from typing import List


x = '-e .'
def get_requirements ( file_path : str ) -> List :
    ''' This function will return the list of requirements '''
    requirements = []
    with open ( file_path ) as file :
        requirements = file.readlines()
        requirements = [ req.replace( "\n" , "" ) for req in requirements ]
        if x in requirements :
            requirements.remove(x)

    return requirements        


setup (
    name = 'ML_project' ,
    version = '0.0.1' ,
    author = 'Rwiddhi' ,
    author_email = 'mitrarwiddhi@gmail.com' ,
    packages = find_packages() ,
    install_requires = get_requirements("requirements.txt" ) ,
)