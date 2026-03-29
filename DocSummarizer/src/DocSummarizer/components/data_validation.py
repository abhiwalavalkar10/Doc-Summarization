import os
from DocSummarizer.logging import logger
from DocSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files(self) -> bool:
        try:
            all_files_present = True
            all_files=os.listdir(os.path.join("artifacts","data_ingestion"))
            for file_name in all_files:
                if file_name not in self.config.ALL_REQUIRED_FILES:
                    all_files_present=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Required file {file_name} is missing in {all_files}")
                else:
                    all_files_present = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"All required files are present in {all_files}")
            return all_files_present
        except Exception as e:
            logger.exception(f"Error during file validation: {e}")
            raise e