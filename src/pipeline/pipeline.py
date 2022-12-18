from src.exception import StoreException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from src.entity.artifact_entity import DataIngestionArtifact
import os,sys
from src.constants.db_constants import *


class TrainPipeline:
    def __init__(self):
        try:
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise StoreException(e,sys)

    def start_data_ingestion(self,)->DataIngestionArtifact:
        try:
            
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info(f"{'>>'*15}DataIngestion Started{'<<'*15}")

            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info(f"{'>>'*15}DataIngestion Completed and artifact:{data_ingestion_artifact}{'<<'*15}")
        except Exception as e:
            raise StoreException(e,sys)

    def run_pipeline(self,):
        try:
            data_ingestion_artificat = self.start_data_ingestion()
            return data_ingestion_artificat
        except Exception as e:
            raise StoreException(e,sys)
