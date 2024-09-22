# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# top-level folder for each specific model found within the models/ directory at
# the top-level of this source tree.

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from setuptools import setup


def read_requirements():
    with open("requirements.txt") as fp:
        content = fp.readlines()
    return [line.strip() for line in content if not line.startswith("#")]


setup(
    name="llama_models",
    version="0.0.18",
    author="Meta Llama",
    author_email="llama-oss@meta.com",
    description="Llama models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/meta-llama/llama-models",
    package_dir={"llama_models": "models"},
    classifiers=[],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    include_package_data=True,
)
