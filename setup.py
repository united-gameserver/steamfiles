import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')
reqs_test = parse_requirements('requirements_test.txt')

setup(
    name='steamfiles',
    version='0.1.4',
    url='https://github.com/leovp/steamfiles',
    license='MIT',

    author='Leonid Runyshkin',
    author_email='runyshkin@gmail.com',

    keywords='steam files valve format parse appinfo vdf acf manifest',
    description='Python library for parsing the most common Steam file formats.',
    long_description=read('README.rst'),

    include_package_data=True,
    package_data={'': ['README.rst', 'LICENSE']},

    platforms=['any'],

    packages=find_packages(exclude=['tests']),
    install_requires=[
        str(req) for req in reqs
        ],

    tests_require=[
        str(req) for req in reqs_test
        ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
