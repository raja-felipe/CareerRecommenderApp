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

MAX_ROWS = 50

JOB_SAVE_PATH = "jobs_data.csv"
COMPANIES = ["EY", "PwC", "Deloitte", "Telstra", "RecordPoint", "Mighty Games"]
ROLES = ["Data Scientist", "Accountant", "Software Engineer", "Consultant"]
MAX_TIME = 30
LOCATIONS = ["Melbourne", "Brisbane", "Sydney"]

COMPANY_COLUMNS_TO_VALUES = {
    "job_id" : [i for i in range(30)],
    "company_name": COMPANIES,
    "role" : ROLES,
    "time_watched" : [i for i in range(15, 31)],
    "location" : LOCATIONS
}

USERS_SAVE_PATH = "users_data.csv"

SEX = ["male", "female"]
AGE = [i for i in range(16, 100)]
DEGREE = ["Data Science", "Accounting", "Game Development", "Finance", "Computer Science"]
YEAR = [1, 2, 3]

USERS_COLUMNS_TO_VALUES = {
    "user_id" : [i for i in range(10)],
    "sex" : SEX,
    "age" : AGE,
    "degree" : DEGREE,
    "year" : YEAR
}

JOINS_SAVE_PATH = "joined_data.csv"

def save_the_df(df : pd.DataFrame, save_path:str) -> None:
    pd.DataFrame.to_csv(df, save_path)
    return

def create_jobs_data(save_path:str, max_rows:int = MAX_ROWS) -> None:
    # Make the dataset
    jobs_list = []
    for _ in range(max_rows):
        curr_row = {}
        for col in COMPANY_COLUMNS_TO_VALUES:
            curr_row[col] = random.choice(COMPANY_COLUMNS_TO_VALUES[col])
        jobs_list.append(curr_row)
    save_the_df(pd.DataFrame(jobs_list), save_path)
    return

def create_user_data(save_path:str, max_rows:int = MAX_ROWS) -> None:
    # Make the dataset
    jobs_list = []
    for _ in range(max_rows):
        curr_row = {}
        for col in USERS_COLUMNS_TO_VALUES:
            curr_row[col] = random.choice(USERS_COLUMNS_TO_VALUES[col])
            if col == "sex":
                curr_row["user_name"] = names.get_full_name(curr_row[col])
        jobs_list.append(curr_row)
    save_the_df(pd.DataFrame(jobs_list), save_path)
    return

def create_joined_data(save_path:str, max_rows: int = MAX_ROWS*10) -> None:
    users_data = pd.read_csv(USERS_SAVE_PATH)
    jobs_data = pd.read_csv(JOB_SAVE_PATH)

    # Now join the data
    assert len(users_data) == len(jobs_data), "DataFrames must have the same number of rows"

    # Shuffle the indices
    shuffled_indices = np.random.permutation(len(users_data))

    # Create the new dataset with random joins
    random_joined_df = pd.concat([users_data.iloc[shuffled_indices].reset_index(drop=True), 
                                jobs_data.iloc[shuffled_indices].reset_index(drop=True)], axis=1).drop(labels=["Unnamed: 0"], axis=1)
    
    # Add time watched, job_link_clicked, and liked
    time_watched = []
    job_link_clicked = []
    liked = []
    for _ in range(len(random_joined_df)):
        time_watched.append(random.randint(0, MAX_TIME))
        job_link_clicked.append(random.randint(0, 1))
        liked.append(random.randint(0, 1))
    
    random_joined_df["time_watched"] = time_watched
    random_joined_df["job_link_clicked"] = job_link_clicked
    random_joined_df["liked"] = liked

    save_the_df(random_joined_df, save_path)

def main():
    create_jobs_data(JOB_SAVE_PATH)
    create_user_data(USERS_SAVE_PATH)
    create_joined_data(JOINS_SAVE_PATH)
    return

if __name__ == "__main__":
    main()

