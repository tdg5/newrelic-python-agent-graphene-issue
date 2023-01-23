from os import path
from typing import Dict, List, Tuple

from setuptools import find_packages, setup


VERSION_PATH = path.join(path.abspath(path.dirname(__file__)), "VERSION")

with open(VERSION_PATH, encoding="utf-8", mode="r") as f:
    VERSION = f.read().strip()

_deps = [
    "dependency-injector~=4.39.1",
    "fastapi==0.78.0",
    "hypercorn==0.13.2",
    "nm-toolkit==1.0.2",
    "pydantic==1.10.2",
    "python-json-logger==2.0.4",
    "PyYaml>=~6.0",
]

_dev_deps = [
    "black==21.5b2",
    "click<8.1",
    "coverage-badge==1.1.0",
    "coverage==6.5.0",
    "darglint==1.8.1",
    "dlint==0.13.0",
    "flake8-comprehensions==3.10.1",
    "flake8-eradicate==1.4.0",
    "flake8-spellcheck==0.28.0",
    "flake8-typing-imports==1.12.0",
    "flake8==3.9.2",
    "isort==5.8.0",
    "mypy~=0.971",
    "pep8-naming==0.13.2",
    "pre-commit==2.20.0",
    "pytest-watch~=4.2.0",
    "pytest~=6.2.0",
    "removestar==1.3.1",
    "safety==2.3.3",
    "types-PyYaml~=6.0",
    "wheel>=0.36.2",
]


def _setup_packages() -> List:
    return find_packages(
        "hello_full_stack",
        include=["hello_full_stack"],
        exclude=["*.__pycache__.*"],
    )


def _setup_extras() -> Dict:
    return {
        "all": [_dev_deps, _deps],
        "deps": _deps,
        "dev": _dev_deps,
    }


def _setup_install_requires() -> List:
    return _deps


def _setup_entry_points() -> Dict:
    return {}


def _setup_long_description() -> Tuple[str, str]:
    return open("README.md", "r", encoding="utf-8").read(), "text/markdown"


setup(
    name="hello-full-stack",
    version=VERSION,
    author="Neuralmagic, Inc.",
    author_email="support@neuralmagic.com",
    description="Hello Full Stack",
    long_description=_setup_long_description()[0],
    long_description_content_type=_setup_long_description()[1],
    keywords="[TODO]",
    license="Apache",
    url="https://github.com/neuralmagic/hello-full-stack",
    package_dir={
        "": "hello_full_stack",
    },
    packages=_setup_packages(),
    extras_require=_setup_extras(),
    include_package_data=True,
    install_requires=_setup_install_requires(),
    entry_points=_setup_entry_points(),
    python_requires=">=3.6.0",
    classifiers=["[TODO]"],
)
