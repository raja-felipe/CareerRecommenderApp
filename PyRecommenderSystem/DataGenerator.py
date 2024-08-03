import random
import pandas as pd
import sys
import os
import names
import numpy as np
import ast

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

MAX_ROWS = 50

JOB_SAVE_PATH = "PyRecommenderSystem/jobs_data.csv"
COMPANIES = ["BY", "ZwC", "Allimotor", "Digifined"]
ROLES = ["Data Scientist", "Accountant", "Software Engineer", "Consultant"]
MAX_TIME = 30
LOCATIONS = ["Melbourne", "Brisbane", "Sydney"]

TAG_DICT = {
    0: "small business", 
    1: "ecommerce", 
    2: "design", 
    3 :"startup", 
    4: "tech"
}

COMPANY_COLUMNS_TO_VALUES = {
    "job_id" : [i for i in range(30)],
    "company_name": COMPANIES,
}

USERS_SAVE_PATH = "PyRecommenderSystem/users_data.csv"

SEX = ["male", "female"]
AGE = [i for i in range(16, 25)]
# PREF_LOCATION = ["Sydney", "Melbourne"]

USERS_COLUMNS_TO_VALUES = {
    "sex" : SEX,
    "age" : AGE,
}

JOINS_SAVE_PATH = "PyRecommenderSystem/users_data.csvjoined_data.csv"

class DataGenerator:
    tag_dict : dict[int : str]

    def __init__(self, tag_dict : dict[int : str]):
        self.tag_dict = tag_dict
        return

    def save_the_df(self, df : pd.DataFrame, save_path:str) -> None:
        pd.DataFrame.to_csv(df, save_path)
        return

    def create_jobs_data(self, save_path:str, max_rows:int = len(COMPANIES)) -> None:
        # Make the dataset
        jobs_list = []
        for i in range(max_rows):
            curr_row = {}
            curr_row["company_id"] = i
            curr_row["company_name"] = COMPANIES[i]
            tag_val = {}
            for tag in self.tag_dict.keys():
                tag_val[tag] = random.randint(0, 1)
            curr_row["company_tags"] = tag_val
            jobs_list.append(curr_row)
        self.save_the_df(pd.DataFrame(jobs_list), save_path)
        return

    def create_user_data(self, save_path:str, max_rows:int = MAX_ROWS) -> None:
        # Make the dataset
        jobs_list = []
        for i in range(max_rows):
            curr_row = {}
            curr_row["user_id"] = i
            for col in USERS_COLUMNS_TO_VALUES:
                curr_row[col] = random.choice(USERS_COLUMNS_TO_VALUES[col])
                if col == "sex":
                    curr_row["user_name"] = names.get_full_name(curr_row[col])
            tag_val = {}
            for tag in self.tag_dict.keys():
                tag_val[tag] = random.randint(0, 1)
            curr_row["user_tags"] = tag_val
            last_100_val = {}
            # Just select one tag for now
            last_100_val[random.randint(0, len(COMPANIES))] = random.randint(0, 1)
            curr_row["last_100"] = last_100_val
            queued_companies = []
            curr_row["queued_companies"] = queued_companies
            jobs_list.append(curr_row)
            # print(curr_row)
        self.save_the_df(pd.DataFrame(jobs_list), save_path)
        return

    # def create_joined_data(self, save_path:str, max_rows: int = MAX_ROWS*10) -> None:
    #     users_data = pd.read_csv(USERS_SAVE_PATH)
    #     jobs_data = pd.read_csv(JOB_SAVE_PATH)

    #     # Now join the data
    #     assert len(users_data) == len(jobs_data), "DataFrames must have the same number of rows"

    #     # Shuffle the indices
    #     shuffled_indices = np.random.permutation(len(users_data))

    #     # Create the new dataset with random joins
    #     random_joined_df = pd.concat([users_data.iloc[shuffled_indices].reset_index(drop=True), 
    #                                 jobs_data.iloc[shuffled_indices].reset_index(drop=True)], 
    #                                 axis=1).drop(labels=["Unnamed: 0"], axis=1)
    
    #     # Add time watched, job_link_clicked, and liked
    #     time_watched = []
    #     job_link_clicked = []
    #     liked = []
    #     for _ in range(len(random_joined_df)):
    #         time_watched.append(random.randint(0, MAX_TIME))
    #         job_link_clicked.append(random.randint(0, 1))
    #         liked.append(random.randint(0, 1))
    
    #     random_joined_df["time_watched"] = time_watched
    #     random_joined_df["job_link_clicked"] = job_link_clicked
    #     random_joined_df["liked"] = liked

    #     self.save_the_df(random_joined_df, save_path)

    def gen_data(self):
        self.create_jobs_data(JOB_SAVE_PATH)
        self.create_user_data(USERS_SAVE_PATH)
        # self.create_joined_data(JOINS_SAVE_PATH)
        return

if __name__ == "__main__":
    DataGenerator(tag_dict=TAG_DICT).gen_data()
    # print(type(ast.literal_eval(pd.read_csv(USERS_SAVE_PATH)["last_100"][0])))

