from setuptools import setup
setup(
    name = 'deva',
    version = '0.1.0',
    packages = ['deva'],
    entry_points = {
        'console_scripts': [
            'deva = deva.__main__:main'
        ]
    })