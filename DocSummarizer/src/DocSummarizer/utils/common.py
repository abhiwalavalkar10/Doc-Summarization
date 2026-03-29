import os
from box.exceptions import BoxValueError
import yaml
from DocSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file. This should be a Path object.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.

    Raises:
        BoxValueError: If the YAML file contains invalid syntax.
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' read successfully.")   
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Invalid YAML syntax in file '{path_to_yaml}': {e}")
        raise
    except FileNotFoundError as e:
        logger.error(f"File not found: '{path_to_yaml}'")
        raise
    except Exception as e:
        logger.error(f"Error occurred while reading YAML file '{path_to_yaml}': {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """
    Creates directories specified in the list of paths.

    Args:
        path_to_directories (list[Path]): A list of Path objects representing the directories to be created.
    Returns:    None
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose := True:
                logger.info(f"Directory '{path}' created successfully or already exists.")
        except Exception as e:
            logger.error(f"Error occurred while creating directory '{path}': {e}")
            raise


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of the file or directory at the specified path in a human-readable format.

    Args:
        path (Path): The path to the file or directory.

    Returns:
        str: The size of the file or directory in a human-readable format (e.g., '10.5 MB').
    """
    try:
        if path.is_file():
            size_bytes = path.stat().st_size
        elif path.is_dir():
            size_bytes = sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
        else:
            logger.warning(f"Path '{path}' is neither a file nor a directory.")
            return "0 B"

        size_units = ['B', 'KB', 'MB', 'GB', 'TB']
        size_index = 0
        while size_bytes >= 1024 and size_index < len(size_units) - 1:
            size_bytes /= 1024
            size_index += 1

        human_readable_size = f"{size_bytes:.2f} {size_units[size_index]}"
        logger.info(f"Size of '{path}': {human_readable_size}")
        return human_readable_size
    except Exception as e:
        logger.error(f"Error occurred while calculating size for '{path}': {e}")
        raise