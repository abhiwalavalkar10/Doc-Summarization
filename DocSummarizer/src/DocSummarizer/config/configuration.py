from DocSummarizer.constants import *
from DocSummarizer.utils.common import read_yaml, create_directories
from DocSummarizer.entity import DataIngestionConfig, DataValidationConfig
import os
import logging

def create_directories_cust(dirs: list[str]):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")
        
class ConfigurationManager:
    def __init__(self, config_file_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        # Ensure artifacts_root is a string
        artifacts_root = (
            self.config["artifacts_root"]
            if isinstance(self.config, dict)
            else self.config.artifacts_root
        )
        # create_directories(list([str(artifacts_root)]))
        print("artifacts_root type:", type(artifacts_root))
        print("artifacts_root value:", artifacts_root)
        create_directories_cust([artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories_cust([str(config.raw_data_dir)])
        data_ingestion_config = DataIngestionConfig(
            raw_data_dir = Path(config.raw_data_dir),
            source_URL = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )
        return data_ingestion_config

        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories_cust([str(config.raw_data_dir)])
        
        data_validation_config = DataValidationConfig(
            raw_data_dir = Path(config.raw_data_dir),
            STATUS_FILE = Path(config.STATUS_FILE),
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )
        return data_validation_config
