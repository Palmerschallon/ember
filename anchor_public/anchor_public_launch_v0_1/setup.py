from setuptools import setup, find_packages

setup(
    name="anchor",
    version="0.1.0",
    author="Palmer Luckey & AI Collaborators",
    description="Living temporal infrastructure for human-AI collaboration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/anchor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.0.0",
        "websockets>=10.0",
    ],
    entry_points={
        "console_scripts": [
            "anchor=anchor.cli:main",
        ],
    },
)