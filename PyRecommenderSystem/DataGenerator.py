import random
import pandas as pd
import sys
import os
import names
import numpy as np
import ast

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Append the directory to the system path
sys.path.append(current_dir)

MAX_ROWS = 50

JOB_SAVE_PATH = os.path.join(current_dir, "jobs_data.csv")
COMPANIES = ["BY", "ZwC", "Allimotor", "Digifined", "Larvitar", "Aviary", "Bank of Melbourne", "Deloitte"]
PARENT_FOLDER = os.path.dirname(current_dir)

VIDEO_QUEUE_FOLDER = PARENT_FOLDER + "\\VideoQueue\\"

VIDEO_STORE_FOLDER = PARENT_FOLDER + "\\VideoStorage\\"

VIDEOS = [
    os.path.join(VIDEO_STORE_FOLDER, "Degree.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "PwCDay.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "GoogleTour.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "TelstraInterview.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "ProspleInternship.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "TelstraSydney.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "MediBankSighting.mp4"),
    os.path.join(VIDEO_STORE_FOLDER, "DeloitteShort.mp4")
]
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

USERS_SAVE_PATH = os.path.join(current_dir, "users_data.csv")

SEX = ["male", "female"]
AGE = [i for i in range(16, 25)]
# PREF_LOCATION = ["Sydney", "Melbourne"]

USERS_COLUMNS_TO_VALUES = {
    "sex" : SEX,
    "age" : AGE,
}

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
            curr_row["video_location"] = VIDEOS[i]
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

    def gen_data(self):
        self.create_jobs_data(JOB_SAVE_PATH)
        self.create_user_data(USERS_SAVE_PATH)
        # self.create_joined_data(JOINS_SAVE_PATH)
        return

if __name__ == "__main__":
    DataGenerator(tag_dict=TAG_DICT).gen_data()
    # print(type(ast.literal_eval(pd.read_csv(USERS_SAVE_PATH)["last_100"][0])))

