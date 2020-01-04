from setuptools import setup

setup(
    name='wayback',
    version='1.1',
    url='https://medium.com/infosec-adventures',
    author='https://github.com/t0thkr1s',
    author_email='t0thkr1s@icoud.com',
    description='Command line program for the Wayback machine.',
    install_requires=['requests', 'colorama', 'tabulate', 'progressbar2']
)
