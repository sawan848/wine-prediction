import urllib.request as request
from WinePrediction import logger
from WinePrediction.utils.common import get_size
from WinePrediction.entity.config_entity import DataIngestionConfig
from WinePrediction.config.configuration import ConfigurationManager
from WinePrediction.components.data_ingestion import DataIngestion


STAGE_NAME="Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx================x")
        
    except Exception as e:
        logger.exception(e)
        
        raise e