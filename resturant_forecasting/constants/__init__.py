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
