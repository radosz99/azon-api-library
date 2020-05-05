from setuptools import setup, find_packages

setup(
    name='azon-library',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python package used to facilitate the use of AZON resources',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/radosz99/azon-api-library',
    author='Radoslaw Lis',
    author_email='241385@student.pwr.edu.pl'
)