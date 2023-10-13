from setuptools import setup, find_packages

setup(
    name='car-data-processor',
    version='1.0',
    packages=find_packages(),
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'car-data-processor=car_data_processor:main'
        ],
    },
)