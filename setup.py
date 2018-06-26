from setuptools import find_packages, setup
from package import Package

setup(name='pyinstall_lockheed_tf',
    version='0.1',
    description='tensorflow for ubuntu 16.04 kernal',
    url='http://github.com/ejlagorga/pyinstall_lockheed_tf',
    author='ejlagorga',
    author_email='john.e.lagorga@lmco.com',
    packages=find_packages(),
    cmdclass={
        "package": Package
    }
)
