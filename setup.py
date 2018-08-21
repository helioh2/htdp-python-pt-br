import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="htdp_pt_br",
    version="0.0.1",
    author="Helio H. Monte-Alto",
    author_email="heliohenrique3@gmail.com",
    description="A library and framework based on the HtDP approach for teaching programming, by Matthias Felleisen et al. It is similar to the htdp_pt_br packages in Racket.",
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