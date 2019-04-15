# -*- coding: utf-8 -*-

import setuptools


with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read()


setuptools.setup(
    name='satsie',
    version='1.0.0',
    author='vjyq',
    author_email='yuqing.ji@outlook.com',
    description='a tool to check for your subscription updates.',
    url='https://github.com/vjyq/satsie.git',
    install_requires=requirements,
    packages=setuptools.find_packages(include=[
        'satsie',
        'satsie.settings',
        'satsie.subscription',
        'satsie.utils',
    ]),   
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='./satsie/tests',
    entry_points={
        'console_scripts': [
            'satsie=satsie.utils:cli',
        ],
    },
)
