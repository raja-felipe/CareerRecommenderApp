import random
import pandas as pd
import sys
import os
import names
import numpy as np

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

# COLUMNS FOR DIFFERENT DATASETS

USERS_COLUMNS = [
	"user_id" : int,
	"name" : str
	"location" : str,
	"sex" : str,
	"date_of_birth" : str,
	"last_100" : dict,
	"user_tags" : dict
]

COMPANY_COLUMNS = [
	"company_id" : int,
	"company_name" : str,
	"company_tags" : dict
]