import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unrar-tool",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="A simple web service that makes it easy to convert rar to zip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/unrar-tool",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/unrar-tool/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["unrar_tool"]),
    install_requires=["aiofiles", "fastapi[all]", "gunicorn", "rich"],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12"
)
