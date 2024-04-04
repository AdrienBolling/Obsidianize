from setuptools import setup, find_packages

setup(
    name='obsidianize'
         '',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nbformat',
        'nbconvert',
        'fire',
        'pandas',
        'matplotlib',
        'plotly',
    ],
    entry_points={
        'console_scripts': [
            'obsidianize = obsidianize.scripts.__main__:main_cli',
        ],
    },
)