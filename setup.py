import os
from setuptools import setup, find_packages
import voot


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="voot",
    version=voot.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='group gmp federation',
    packages=find_packages(),
    author='Johan Berggren',
    author_email='jbn@nordu.net',
    url="",
    include_package_data=True,
    test_suite='voot.tests.runtests.runtests',
)
