from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dummy_python',
    version='0.1.0',
    description='Dummy package for Python project structure',
    long_description=readme,
    author='Rohit Kamal Saxena',
    author_email='rohit_kamal2003@yahoo.com',
    url='https://github.com/rksaxena/python_dummy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
