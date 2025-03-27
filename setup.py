from setuptools import find_packages, setup
from pathlib import Path

here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="midrc_react",
    version="0.1.0",
    description="The MIDRC Representativeness Exploration and Comparison Tool (REACT) is a tool designed to compare the representativeness of biomedical data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robert Tomek",
    author_email="rtomek@uchicago.edu",
    url="https://github.com/MIDRC/MIDRC-REACT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy>=1.26.0",
        "pandas>=2.2.0",
        "PySide6>=6.6.0",
        "scipy>=1.12.0",
        "openpyxl>=3.1.0",
        "pytest>=8.1.0",
        "PyYAML>=6.0.0",
        "prince>=0.15.0",
        "dash>=2.18.2",
        "plotly>=5.24.1",
        "matplotlib>=3.9.0",
        "seaborn>=0.13.2",
        "ipywidgets>=8.1.5",
        "ipython>=8.28.0",
        "python-dateutil>=2.9.0.post0",
        "tabulate>=0.9.0",
        "scikit-learn>=1.6.1",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "midrc-react=midrc_react.gui.pyside6.launch_react:launch_react",
            "MIDRC-REACT=midrc_react.gui.pyside6.launch_react:launch_react",
        ],
    },
)
