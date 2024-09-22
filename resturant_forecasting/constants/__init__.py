import os
from datetime import date  

DATABASE_NAME = 'resturant'
COLLECTION_NAME = 'restaurant_forecast'
MONGODB_URL_KEY = 'MONGODB_URL'
PIPELINE_NAME:str = 'resturant_forecasting'
ARTIFACT_DIR:str = 'artifacts'

MODEL_FILE_NAME = 'model.pkl'
TARGET_COLUMN = 'year_3_profit'

CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'

FILE_NAME: str = 'restaurant_success.csv'
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'

"""
This file contains all the constants that are used in the project.
"""
DATA_INGESTION_COLLECTION_NAME:  str = 'restaurant_forecasting'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = 'features_store'
DATA_INGESTION_INGESTION_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2