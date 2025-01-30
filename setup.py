from setuptools import setup, find_packages

setup(
    name="xHunter",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds packages
    install_requires=[
        'scapy',
        'python-nmap',
        'requests'
    ],
    entry_points={
        'console_scripts': ['xHunter = xHunter.cli:main']
    },
    package_data={
        'xHunter': ['wordlists/*.txt']
    },
    python_requires='>=3.6',
)