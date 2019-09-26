try:
    import setuptools
except ImportError:
    print("Install setuptools library")

install_requires = [
    'matplotlib>=1.4.3',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

# packages = []

if __name__ == "__main__":
    setuptools.setup(
        name="phdTools",
        version="0.0.2",
        author="Ioannis Antonopoulos",
        author_email="anton.ioannis.phys@gmail.com",
        description="A collection of tools during PhD",
        long_description=long_description,
        long_description_content_type="text/markdown",
        download_url="https://github.com/antongiannis/phd_tools/",
        packages=setuptools.find_packages(),
		install_requires=install_requires
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
    )
