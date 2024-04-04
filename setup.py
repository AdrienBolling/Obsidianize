from setuptools import setup, find_packages

setup(
    name='obsidianize',
    description='A package to convert jupyter notebooks to markdown files for use in Obsidian',
    version='1.0.0',
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
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
