from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1", "scikit-learn>=1", "pandas>=1.2"]

setup(name='gs-ds-tools',
      version='0.0.1',
      description='My DS and ML tools for Kaggle-like competitions',
      long_description=readme,
      long_description_content_type="text/markdown",
      author='Gleb Shigin',
      author_email='gs.shigin@students.cosmos.msu.ru',
      url='https://github.com/gshigin/gs-ds-tools',
      packages=find_packages(),
      install_requires=requirements,
      classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
     )