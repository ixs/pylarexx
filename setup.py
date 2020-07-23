#!/usr/bin/env python3
"""setup.py file."""

from setuptools import setup, find_packages
import re
import uuid

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=uuid.uuid1())
try:
    reqs = [str(ir.req) for ir in install_reqs]
except AttributeError:
    reqs = [str(ir.requirement) for ir in install_reqs]

with open("pylarexx.py", "r") as f:
    content = f.read()
    metadata = re.findall(r"^__([a-z]+)__ = [']*([^'\[]+)[']*$", content, re.MULTILINE)
    metadata.extend(re.findall(r"^@([a-z]+):\s+(.*)$", content, re.MULTILINE))
    metadata = dict(metadata)

with open("Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="Pylarexx",
    author=metadata["author"],
    version=metadata["version"],
    license=metadata["license"],
    packages=find_packages(),
    scripts=["pylarexx.py"],
    description="Python DataLogger for Arexx Multilogger Devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="arexx datalogger multilogger",
    url="https://github.com/redflo/pylarexx",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
    ],
    install_requires=reqs,
)
