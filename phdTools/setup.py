import setuptools

with open(".../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="phdTools",
    version="0.0.1",
    author="Ioannis Antonopoulos",
    author_email="anton.ioannis.phys@gmail.com",
    description="A collection of tools during PhD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
