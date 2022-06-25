# Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, List, Tuple

from setuptools import find_packages, setup


_deps = [
    "fastapi",
    "hypercorn",
]


_dev_deps = [
    "awscli>=1.19.24",
    "black==21.5b2",
    "flake8==3.9.2",
    "isort==5.8.0",
    "rinohtype~=0.4.2",
    "sphinxcontrib-apidoc~=0.3.0",
    "wheel>=0.36.2",
    "pypiserver>=1.4.2",
    "pytest~=6.2.0",
    "pytest-mock~=3.6.0",
    "click<8.1",
]


def _setup_packages() -> List:
    return find_packages(
        "src",
        include=[],
        exclude=["*.__pycache__.*"],
    )


def _setup_extras() -> Dict:
    return {"dev": _dev_deps, "deps": _deps, "all": [_dev_deps, _deps]}


def _setup_install_requires() -> List:
    return _deps


def _setup_entry_points() -> Dict:
    return {}


def _setup_long_description() -> Tuple[str, str]:
    return open("README.md", "r", encoding="utf-8").read(), "text/markdown"


setup(
    name="hello-full-stack",
    version="1.0",
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
