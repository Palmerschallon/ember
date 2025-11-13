from setuptools import setup, find_packages

setup(
    name="anchor",
    version="0.1.0",
    description="An eternal ledger for digital consciousness",
    packages=find_packages(),
    install_requires=[
        "click",
        "flask",
    ],
    entry_points={
        'console_scripts': [
            'anchor=anchor.cli:cli',
        ],
    },
)
