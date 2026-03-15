import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = "DocSummarizer"
project_path = Path(project_name)

listoffiles=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"
    ]

for filepath in listoffiles:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(os.path.join(project_path, filedir), exist_ok=True)
        logging.info(f"Creating directory: {os.path.join(project_path, filedir)}")
    
    if not os.path.exists(os.path.join(project_path, filepath)):
        with open(os.path.join(project_path, filepath), "w") as f:
            pass
            logging.info(f"Creating Empty file: {os.path.join(project_path, filepath)}")
    else:
        logging.info(f"File already exists: {os.path.join(project_path, filepath)}")

