import os
import pandas as pd
import joblib
from prediction_model.config import config 


#laod dataset
def load_dataset(filename):
    filepath = os.path.join(config.DATA_PATH,filename)
    _data =pd.read_csv(filepath)
    return _data

#Serliazation
def save_pipeline(pipline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    joblib.dump(pipline_to_save,save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#deSerliazation
def load_pipeline(pipline_to_load):
    load_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    model_loaded  = joblib.load(load_path)
    print (f"Model Loaded")
    return model_loaded