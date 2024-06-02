from setuptools import setup, find_packages

# find src folder with __init__.py and requirements.txt

setup(
    name = "Generative AI Project",
    version = "0.0.0",
    author = 'Sanjay Tandon',
    packages = find_packages(),        ## automatically find all the local packages in the src folder
    install_requires = [],             ## looks for requirements.txt file and installs all the packages listed there.
)
    