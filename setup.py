from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="telegraph",
    version="0.1.0",
    author="My Name",
    author_email="your.email@example.com",
    description="A Python wrapper for the Telegra.ph API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/telegraph-api-wrapper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests==2.26.0",
    ],
)
