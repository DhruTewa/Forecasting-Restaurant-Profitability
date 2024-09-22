from resturant_forecasting.configuration.mongodb_connection import MongoDBClient
from resturant_forecasting.constants import *
from resturant_forecasting.exception import ResturantForecastException
import pandas as pd
import sys
import numpy as np
from typing import Optional

class ResturantData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except ResturantForecastException as e:
            raise ResturantForecastException(e,sys)
            
    def export_collection_as_dataframe(self,collection_name:str,database_name = Optional[str]==None)->pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns=["_id"],inplace=True)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise ResturantForecastException(e,sys)
                
   