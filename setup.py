from setuptools import find_packages, setup

setup(
    name='midrc_react',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        # list additional dependencies here, for example:
        # 'numpy',
        # 'pandas',
    ],
    entry_points={
        'console_scripts': [
            'midrc-react=midrc_react.gui.pyside6.launch_react:launch_react',
            'MIDRC-REACT=midrc_react.gui.pyside6.launch_react:launch_react',
        ],
    },
)
