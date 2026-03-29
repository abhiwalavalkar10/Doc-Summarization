from DocSummarizer.config.configuration import ConfigurationManager
from DocSummarizer.logging import logger
from DocSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            transformation_config = self.config.get_data_transformation_config()
            data_transformation = DataTransformation(config=transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.exception(e)
            raise e
