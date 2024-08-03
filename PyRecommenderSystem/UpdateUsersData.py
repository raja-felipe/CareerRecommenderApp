import os
import sys
import argparse
import pandas as pd
import ast
from DataGenerator import USERS_SAVE_PATH, JOB_SAVE_PATH

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

def update_users_data(user_id : int, company_id : int, percent_watched: float, 
                      bookmarked: int, liked : int, clicked_link : int) -> None:
    # First get the length of the video watched
    new_rating = -1 + (0.4 + 1)*(percent_watched)
    remaining_to_add = 0.2
    new_rating += remaining_to_add*(bookmarked + liked + clicked_link)

    # Now that we have the new rating, we update the tags relevant to the role
    jobs_data = pd.read_csv(JOB_SAVE_PATH)
    users_data = pd.read_csv(USERS_SAVE_PATH)
    # print(jobs_data[jobs_data["company_id"] == company_id])
    user_tags = users_data[users_data["user_id"] == user_id]["user_tags"].values[0]
    jobs_tags = jobs_data[jobs_data["company_id"] == company_id]["company_tags"].values[0]
    jobs_tags = ast.literal_eval(jobs_tags)
    user_tags = ast.literal_eval(user_tags)
    # print(jobs_tags)
    # print(user_tags)

    # For now, just assign the new value
    for tag in user_tags.keys():
        # print(tag)
        if jobs_tags[tag] == 1:
            user_tags[tag] = new_rating
    # print(user_tags)
    
    # Now we have the new tags, we have to adjust the dataframe
    users_data.loc[users_data["user_id"] == user_id, "user_tags"] = str(user_tags)
    users_data.to_csv(USERS_SAVE_PATH)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update dataframe with new tag ratings')
    parser.add_argument('user_id', type=int)
    parser.add_argument('company_id', type=int)
    parser.add_argument('percent_watched', type=float)
    parser.add_argument('bookmarked', type=int, help="0 or 1 only")
    parser.add_argument('liked', type=int, help="0 or 1 only")
    parser.add_argument('clicked_link', type=int, help="0 or 1 only")
    
    args = parser.parse_args()
    
    user_id = args.user_id
    company_id = args.company_id
    percent_watched = args.percent_watched
    bookmarked = args.bookmarked
    liked = args.liked
    clicked_link = args.clicked_link

    update_users_data(user_id, company_id, percent_watched, bookmarked, liked, clicked_link)