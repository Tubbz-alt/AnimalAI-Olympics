from setuptools import setup

setup(
    name="animalai_train",
    version="2.0.0b0",
    description="Animal AI competition training library",
    url="https://github.com/beyretb/AnimalAI-Olympics",
    author="Benjamin Beyret",
    author_email="bb1010@ic.ac.uk",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["animalai_train"],  # Required
    zip_safe=False,
    install_requires=["animalai==2.0.0b0", "mlagents==0.15.0"],
    python_requires=">=3.6.1",
)
