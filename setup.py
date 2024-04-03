from setuptools import setup, find_packages

setup(
    name='jupyter_displays_for_obsidian',
    version='0.2',
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
            'jupyter_to_obsidian = jupyter_to_obsidian.scripts.convert:main_cli',
            'setup_jupyter_to_obsidian = jupyter_to_obsidian.scripts.setup:main_cli',
            'refresh_jupyter_to_obsidian = jupyter_to_obsidian.scripts.convert:main_cli'
        ],
    },
)