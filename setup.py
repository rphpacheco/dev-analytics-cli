from setuptools import setup
setup(
    name = 'dev-analytics-cli',
    version = '0.1.0',
    packages = ['features'],
    entry_points = {
        'console_scripts': [
            'deva = features.__main__:main'
        ]
    })