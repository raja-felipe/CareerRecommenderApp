import pandas as pd
from DataConstants import USER_COLUMNS
from DataGenerator import JOB_SAVE_PATH, JOINS_SAVE_PATH, USERS_SAVE_PATH, save_the_df
import os
import sys

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

SIM_MATRIX_PATH = "sim_matrix.csv"

class UsersDataBase:
    def __init__(self):
        users_columns : list[str]
        users_df : pd.DataFrame

        # Most likely store the data in a pandas dataframe
        self.users_columns : list[str] = pd.read_csv(USERS_SAVE_PATH)
        self.users_df = None
        return
    
    def make_users_data(self, count=50):
        return

if __name__ == "__main__":
    rec_sys = UserRecommenderSystem()
    print(rec_sys.get_unique_job_ids())
    