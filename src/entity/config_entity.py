from src.exception import StoreException
from src.logger import logging
import os,sys
from datetime import datetime
from src.constants import *


class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime.now()):
        try:
            timestamp = timestamp.strftime('%m_%d_%Y-%H_%M_%S')
            self.artifact_dir_path = os.path.join(DATA_INGESTION_ARTIFACT_DIR_NAME,timestamp)
            self.timestamp = timestamp    
        except Exception as e:
            raise StoreException(e,sys)

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            logging.info(f"{'>>'*30}DataIngestionConfig Started{'<<'*30}")
            self.data_ingestion_dir = os.path.join(
                training_pipeline_config.artifact_dir_path,DATA_INGESTION_DIR_NAME
            )
            self.feature_store_file_path = os.path.join(
                self.data_ingestion_dir,DATA_INGESTION_FEATURE_STORE,
                FILE_NAME
            )
            self.training_file_path = os.path.join(
                self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,
                TRAIN_FILE_NAME
            )
            self.testing_file_path = os.path.join(
                self.data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,
                TEST_FILE_NAME
            )
            self.train_test_split_ratio:float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
            
            logging.info(f"{'>>'*30}DataIngestionConfig Ended{'<<'*30}")
        except Exception as e:
            raise StoreException(e,sys)