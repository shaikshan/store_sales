from datetime import datetime
import os

ROOT_DIR = os.getcwd()

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#Data Ingestion constants

DATA_INGESTION_ARTIFACT_DIR_NAME = "artifact"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_INGESTED_DIR = "ingested_dir"
DATA_INGESTION_FEATURE_STORE = "feature_store"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
FILE_NAME = "Sales.csv"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2



