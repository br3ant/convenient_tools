from setuptools import setup, find_packages

setup(
    name="convenient_tools",
    version="0.1",
    author="Br3ant",
    author_email="1106617567@qq.com",
    description="A convenient Python utility library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/br3ant/convenient_tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
