from setuptools import find_packages, setup

setup(
    name="Bertalign",
    version="0.1.0",
    url="https://github.com/hrabalm/bertalign",
    description="An automatic mulitlingual sentence aligner.",
    packages=find_packages(),
    install_requires=[
        "numba>=0.56.4",
        "faiss-gpu>=1.7.2",
        "sentence-splitter>=1.4",
        "sentence-transformers>=2.2.2",
    ],
)
