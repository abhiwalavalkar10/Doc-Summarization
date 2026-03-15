import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_= "0.0.0"
REPO_NAME= "DocSummarizer"
AUTJHOR_USER_NAME= "abhiwalavalkar10"
SRC_REPO= "DocSummarizer"
AUTHOR_EMAIL="abhiwalavalkar10@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTJHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for document summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTJHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTJHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
