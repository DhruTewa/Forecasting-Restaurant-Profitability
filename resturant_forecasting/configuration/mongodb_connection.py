import os
from resturant_forecasting.constants import *
import sys
from resturant_forecasting.exception import ResturantForecastException
from resturant_forecasting.logger import logging
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME)->None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception("MongoDB URL is not set in environment variable")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection established successfully")
        except Exception as e:
            raise ResturantForecastException(e,sys)
    