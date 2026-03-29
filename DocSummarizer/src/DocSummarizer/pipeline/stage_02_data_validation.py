from DocSummarizer.config.configuration import ConfigurationManager
from DocSummarizer.logging import logger
from DocSummarizer.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            validation_config = self.config.get_data_validation_config()
            data_validation = DataValidation(config=validation_config)
            data_validation.validate_all_files()
        except Exception as e:
            logger.exception(e)
            raise e
