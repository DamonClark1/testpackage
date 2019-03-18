from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA practise recursion/sorting python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/DamonClark1/testpackage',
    author='Damon Clark',
    author_email='damon.clark69@gmail.com'
)
