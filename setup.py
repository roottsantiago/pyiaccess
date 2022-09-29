import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyiAccess",
    version="0.2",
    author="Tomás Santiago González",
    author_email="thom.sgonzalez@gmail.com",
    description="It is a library that connects to IBM Power Systems (IBM i), with pyodbc and SSH connection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomgonzalez/pyiaccess",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Operating System Kernels :: Linux"
    ],
    python_requires='>=3.4',
    install_requires=[
        'python-dotenv',
        'pyodbc',
        'paramiko'
    ],
    keywords=['IBM i Access', 'iSeries', 'systems i', 'AS/400'],
    project_urls={
        'Homepage': 'https://github.com/thomgonzalez/pyiaccess',
    },
)
