import pandas as pd
from DataGenerator import JOB_SAVE_PATH, JOINS_SAVE_PATH, USERS_SAVE_PATH, save_the_df
import os
import sys

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

SIM_MATRIX_PATH = "sim_matrix.csv"

class UserRecommenderSystem:
    def __init__(self):
        # Most likely store the data in a pandas dataframe
        self.users : pd.DataFrame = pd.read_csv(USERS_SAVE_PATH)
        self.jobs : pd.DataFrame= pd.read_csv(JOB_SAVE_PATH)
        self.joins : pd.DataFrame = pd.read_csv(JOINS_SAVE_PATH)
        self.sim_matrix : pd.DataFrame = self.create_similarity_matrix()
        return
    
    def get_unique_job_ids(self):
        return list(set(self.jobs["job_id"]))
    
    def create_similarity_matrix(self):
        unique_jobs = self.get_unique_job_ids()
        seen = set()
        new_df = []
        # Go through every single user
        for _, row in self.users.iterrows():
            curr_id = row["user_id"]
            if not curr_id in seen:
                seen.add(row["user_id"])
                # Filter joins to only 
                curr_joins = self.joins[self.joins["user_id"] == curr_id]
                # Now add the values in a dictionary
                new_row = {}
                new_row["user_id"] = curr_id
                for job in unique_jobs:
                    job_row = curr_joins[curr_joins["user_id"] == job]
                    if not job_row.empty:
                        # Now add the value we want to associate with it
                        job_row_vals = job_row.iloc[0]
                        # NOTE: ADD COEFFICIENTS HERE???
                        job_val = job_row_vals["time_watched"] + \
                            job_row_vals["job_link_clicked"] + \
                            job_row_vals["liked"]
                        new_row[job] = job_val
                    else:
                        new_row[job] = 0
                new_df.append(new_row)
        self.sim_matrix = pd.DataFrame(new_df)
        save_the_df(self.sim_matrix, SIM_MATRIX_PATH)
        return
    
    def get_sim_matrix_of_user(self, user_id:int):
        return self.sim_matrix[self.sim_matrix["user_id"] == user_id]
    
    def mean_center_row(self, array):
        mean = sum(array)/len(array)
        return [item-mean for item in array if item != 0]
    
    def get_most_similar_user(self, user_id:int) -> int:
        user_row = self.get_sim_matrix_of_user(user_id)
        user_row_values = self.mean_center_row(user_row.values()[1:])
        min_cos_sim = float("inf")


        for _, row in self.sim_matrix.iterrows():
            if row != user_row:
                curr_row_values = list(row.values())[1:]
                curr_row_values = self.mean_center_row(curr_row_values)
                # Now apply logic to add
                user_numerator = 0
                row_numerator = 0
                for i in range(len(curr_row_values)):
                    user_val = user_row_values[i]
                    row_val = curr_row_values[i]
                    if user_val == 0:
                        continue
        return

if __name__ == "__main__":
    rec_sys = UserRecommenderSystem()
    print(rec_sys.get_unique_job_ids())
    