from setuptools import setup, find_packages

setup(
    name="axe_builder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer==0.9.0",
        "lark-parser==1.1.5",
        "textual==0.2.1",
        "loguru==0.6.0",
        "pydantic==1.10.2",
        "pytest==7.1.2",
        "hypothesis==6.52.2",
        "jinja2==3.1.2",
        "sphinx==4.5.0",
        "sphinx-autodoc-typehints==1.19.2"
    ],
    entry_points={
        "console_scripts": [
            "axe-builder=axe_builder.cli:app",
        ],
    },
    author="Your Name",
    author_email="you@example.com",
    description="A CLI Menu Builder using axe:Syntax",
    license="MIT",
    keywords="cli, typer, lark, textual, loguru",
    url="https://github.com/yourusername/axe_builder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
