from src.exception import StoreException
from src.logger import logging
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
import os,sys
from src.database.mongodb import MongoDB
from src.constants.db_constants import *
from src.constants import *
import pandas as pd
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig,):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.mongodb = MongoDB(mongodb_url = MONGO_DB_URL,db_name=DATABASE_NAME,col_name=COLLECTION_NAME)
        except Exception as e:
            raise StoreException(e,sys)
    
    def export_data_into_feature_store(self,):
        """
        Export mongodb collection record as data frame into feature sotre
        """
        try:
            dataframe = self.mongodb.fetch_all_into_dataframe()
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            #creating folders
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise StoreException(e,sys)
    
    def split_data_as_train_and_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set = train_test_split(
                dataframe,test_size = self.data_ingestion_config.train_test_split_ratio
                )
            logging.info("Performed train and test split")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting training and testing data into their dirs")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path,index=False,header=True
            )

            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info("Exported train test files.")

        except Exception as e:
            raise StoreException(e,sys)
    
    def initiate_data_ingestion(self,)->DataIngestionArtifact:
        try:
            logging.info(f"{'>>'*30}DataIngestion Started{'<<'*30}")
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_and_test(dataframe=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info(f"DataIngestionArtifact:{data_ingestion_artifact}")
            logging.info(f"{'>>'*30}DataIngestion Ended{'<<'*30}")    

            return data_ingestion_artifact
        except Exception as e:
            raise StoreException(e,sys)

    
