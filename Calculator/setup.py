from setuptools import setup, find_packages
setup(
    name='calculator',
    version='0.1.0',
    description='A simple python calculator using modularization technique.',
    author='Muhammad Jawad <Your name>',
    author_email='youremail@example.com',
    url='https://github.com/',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'python-dateutil',
        'pytz',
        'scikit-learn',
        'scipy',
        'setuptools',
        'six',
        'threadpoolctl',
        'tzdata',
        'wheel',
        'pytest',
        'joblib',
    ]
    

)