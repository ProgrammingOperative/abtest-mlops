from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirement_file:
    requirements_list = requirement_file.readlines()
    requirements_list = [lib.replace("\n", "") for lib in requirements_list]

requirements = requirements_list

setup(
    name="SmartAd Campaign Performance",
    version="0.1.0",
    description="A/B testing using machine learning on a dataset of users who were shown a creative ad made by the company SmartAd",
    url="https://github.com/ProgrammingOperative/abtest-mlops-Group-Repo",
    author="10 Academy Batch 5 Group 9",
    author_email="hairaer02@gmail.com, taddeekb@gmail.com, wachura11t@gmail.com, nahom.fix@gmail.com",
    license="MIT License",
    install_requires=requirements,
    long_description=readme,
)
