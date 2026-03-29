import pandas as pd
import numpy as np
import os
# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LOG_FILE = os.path.join(DATA_DIR, 'predictions.csv')
REF_FILE = os.path.join(MODELS_DIR, 'reference_data.csv')
def get_recent_predictions(limit: int = 50) -> list

"""Returns the last N prediction records as a list of dictionaries."""