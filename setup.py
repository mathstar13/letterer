import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letterer", # Replace with your own username
    version="0.0.1",
    author="greatusername",
    author_email="alexander.destefano@gmail.com",
    description="More string methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathstar13/letterer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.5',
)