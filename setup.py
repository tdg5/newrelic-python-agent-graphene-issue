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
    "nm-toolkit~=0.2.12",
    "pydantic==1.9.1",
    "PyYaml>=~6.0",
]

_dev_deps = [
    "black==21.5b2",
    "click<8.1",
    "flake8==3.9.2",
    "isort==5.8.0",
    "mypy~=0.971",
    "pytest~=6.2.0",
    "pytest-watch~=4.2.0",
    "types-PyYaml~=6.0",
    "wheel>=0.36.2",
]


def _setup_packages() -> List:
    return find_packages(
        "src",
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
    description=("Fullstack example and template repo."),
    long_description=_setup_long_description()[0],
    long_description_content_type=_setup_long_description()[1],
    keywords="[TODO]",
    license="Apache",
    url="https://github.com/neuralmagic/hello-full-stack",
    package_dir={
        "": "src",
    },
    packages=_setup_packages(),
    extras_require=_setup_extras(),
    include_package_data=True,
    install_requires=_setup_install_requires(),
    entry_points=_setup_entry_points(),
    python_requires=">=3.6.0",
    classifiers=["[TODO]"],
)
