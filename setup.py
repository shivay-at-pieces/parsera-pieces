from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="parsera-pieces",  # New unique name
    version="0.0.1",
    author="Shivay at Pieces",
    author_email="shivay@pieces.app",
    description="Fork of the original Parsera Lightweight library for scraping web-sites with Pieces QGPT LLM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pieces-app/parsera-pieces",
    packages=find_packages(),  # This will include all sub-packages
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10",
    install_requires=[
        "langchain>=0.2.6",
        "langchain-openai>=0.1.8",
        "playwright>=1.44.0",
        "playwright-stealth>=1.0.6",
        "markdownify>=0.12.1",
        "pieces-copilot-sdk>=0.5.0",
    ],
)