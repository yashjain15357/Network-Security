"""
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or distutils in older python version ) to define the configuration of ypu project, 
such as its metadata, dependencies, and more
"""
from setuptools import setup , find_packages
from typing import List

def get_requirements()->list[str]:
    """This function return list of requirements"""
    req_list = []
    try:
        with open("requirements.txt" , 'r') as file:
            # read line from the file
            lines = file.readlines()

            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty line and -e.
                if(requirement and requirement!="-e ."):
                    req_list.append(requirement)
            return req_list
    except FileNotFoundError:
        print("requirements.txt file not found")

# print(get_requirements())
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Yash jain",
    author_email="jainy9089@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)