import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "remove_bg",
    version = "1.0.0",
    author = "MyFaduGame",
    author_email = "navinsharma9376319931@gmail.com",
    description = "Remove Background with Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://www.github.com/MyFaduGame/remove_bg",
    install_requires = [
        "pillow",
        "rembg",
    ],
    project_urls = {
        "Bug Tracker": "https://www.github.com/MyFaduGame/remove_bg",
    },
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    keywords="remove, background, u2net, MyFaduGame, myfadugame, Navin",
)