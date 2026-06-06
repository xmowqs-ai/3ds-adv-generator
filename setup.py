from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="3ds-adv-generator",
    version="0.1.0",
    author="xmowqs-ai",
    description="Python-based 3DS ADV game generator with C language compilation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xmowqs-ai/3ds-adv-generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "3ds-adv-gen=adv_generator.cli:main",
        ],
    },
)
