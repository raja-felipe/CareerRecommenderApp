from sklearn.cluster import KMeans
import pandas as pd
from DataGenerator import JOB_SAVE_PATH, USERS_SAVE_PATH
import ast
import pickle

MODEL_SAVE_PATH = "PyRecommenderSystem/user_kmeans.pkl"

class UserRecommenderCluster:
    users_data : pd.DataFrame
    jobs_data : pd.DataFrame
    cluster_values : int
    kmeans : KMeans

    def __init__(self, users_data_path:str = USERS_SAVE_PATH,
                jobs_data_path:str = JOB_SAVE_PATH, cluster_values:int = 5):
        self.users_data = pd.read_csv(users_data_path)
        self.jobs_data = pd.read_csv(jobs_data_path)
        self.kmeans = KMeans(n_clusters=cluster_values)
        return
    
    # Helper Function to parse string dicts
    def parse_string_dict(self, dict_str:str) -> dict:
        return ast.literal_eval(dict_str)
    
    # KMeans Clustering
    def create_kmeans_cluster(self):
        # First get the user tags data list
        # without_user = self.users_data[self.users_data["used_id"] != user_id]
        tags_data = list(self.users_data["user_tags"])
        tags_data = [ast.literal_eval(item) for item in tags_data]
        tags_data = pd.DataFrame(tags_data)
        self.kmeans.fit(tags_data)
        # with open(MODEL_SAVE_PATH, "wb") as fp:
        #     pickle.dump(self.kmeans, fp)
        # print(ast.literal_eval(tags_data[0]))
        return
    
    # Select n_closest nodes
    def select_n_closest(self, curr_id:int, num_closest:int=10):
        # Get a mapping of the vector str to the vector
        tag_to_ids = {}
        vector_str = self.users_data["user_tags"]
        for tag in vector_str:
            ids_with_same_tags = list(self.users_data[self.users_data["user_tags"] == tag]["user_id"])
            tag_to_ids[tag] = ids_with_same_tags       

        # 
    
if __name__ == "__main__":
    UserRecommenderCluster().create_kmeans_cluster()