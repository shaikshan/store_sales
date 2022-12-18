import pandas as pd
import os
import pymongo
from src.constants import *
from src.exception import StoreException
from src.logger import logging
import sys


class MongoDB:
    def __init__(self,mongodb_url:str=None,db_name:str=None,col_name:str=None,):
        try:
            self.mongodb_url = mongodb_url
            self.my_client = pymongo.MongoClient(self.mongodb_url)
            self.db_name = db_name
            self.my_db = self.my_client[self.db_name]
            self.col_name = col_name
            self.my_col = self.my_db[self.col_name]
        except Exception as e:
            raise StoreException(e,sys)
    
    def fetch_all_into_dataframe(self,):
        for data in self.my_col.find():
            del data["_id"]
            dataframe = pd.DataFrame(data)
        return dataframe
