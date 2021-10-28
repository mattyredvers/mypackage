from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='EDSA example pythonpackage',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='http://github.com/<username>/<package-name>',
    author='<Your Name',
    author_email='<Your Email'
)

