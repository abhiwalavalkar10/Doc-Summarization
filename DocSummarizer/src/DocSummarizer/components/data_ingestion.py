import os
import urllib.request as request
import zipfile
from pathlib import Path
# from DocSummarizer.config.configuration import ConfigurationManager
from DocSummarizer.logging import logger
from DocSummarizer.utils.common import get_size
from DocSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def unzip_and_clean(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Unzipped file and cleaned up the zip file")
        os.remove(self.config.local_data_file)