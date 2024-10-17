from setuptools import setup, find_packages

setup(
    name="farmergame",
    version="0.1",
    package_dir={"": "src"},  # Indicate that packages are under the 'src' directory
    packages=find_packages(where='src'),  # Find packages in the 'src' directory
    author="Quinn Cuijpers",  # Replace with your name
    author_email="Quinn.Cuijpers@gmail.com",  # Replace with your email
    description="A package to solve the farmer's problem.",
    # long_description=open("README.md").read(),  # Assumes you have a README file
    long_description_content_type='text/markdown',
    url="https://github.com/QuinnCuijpers/farmergame",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
    install_requires=[
        # Add your project's dependencies here
        # "somepackage>=1.0.0",
    ],
)

