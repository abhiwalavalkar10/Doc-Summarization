from DocSummarizer.config.configuration import ConfigurationManager
from DocSummarizer.logging import logger
from DocSummarizer.utils.common import get_size
from DocSummarizer.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
    
    def main(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_and_clean()
        except Exception as e:
            logger.exception(e)
            raise e
