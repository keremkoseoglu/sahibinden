""" Setup module """
import setuptools

setuptools.setup(
    name="sahibinden-keremkoseoglu",
    version="0.0.1",
    author="Kerem Koseoglu",
    author_email="kerem@keremkoseoglu.com",
    description="sahibinden.com Web spider",
    long_description="sahibinden.com web spider",
    long_description_content_type="text/markdown",
    url="https://github.com/keremkoseoglu/sahibinden",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    include_package_data=True
)