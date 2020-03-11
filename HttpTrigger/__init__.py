import logging

import azure.functions as func

import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import pathlib

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    loaded_model = pickle.load(open("/home/site/wwwroot/HttpTrigger/xgbTL_Boston.pkl", "rb"))

    return func.HttpResponse("function running!")