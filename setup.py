import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-dynamicfield",
    version="1.0.0",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    description="Create dynamic fields from django admin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/null-none/django-dynamicfield",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
