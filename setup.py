import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="astrakpy",
    version="0.1",
    author="TriedGrief",
    author_email="triedgrief@yandex.ru",
    description="AstrakPy async library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/triedgriefdev/astrakpy",
    packages=["astrakpy"],
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
