from sklearn.cluster import KMeans
import pandas as pd
from DataGenerator import JOB_SAVE_PATH, USERS_SAVE_PATH, COMPANY_COLUMNS_TO_VALUES, COMPANIES
import ast
import pickle
import os
import sys

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Append the directory to the system path
sys.path.append(current_dir)

MODEL_SAVE_PATH = "user_kmeans.pkl"
SAMPLE_VAL = 5

class RecommenderSystem:
    users_data : pd.DataFrame
    jobs_data : pd.DataFrame
    cluster_values : int
    curr_cluster : int
    closest_histories : list[dict[int, int]]
    kmeans : KMeans
    recommendations : list[int]

    def __init__(self, users_data_path:str = USERS_SAVE_PATH,
                jobs_data_path:str = JOB_SAVE_PATH, cluster_values:int = 5):
        self.users_data = pd.read_csv(users_data_path)
        self.jobs_data = pd.read_csv(jobs_data_path)
        self.kmeans = KMeans(n_clusters=cluster_values)
        self.recommendations = []
        return
    
    # Helper Function to parse string dicts
    def parse_string_dict(self, dict_str:str) -> dict:
        return ast.literal_eval(dict_str)
    
    # KMeans Clustering
    def create_kmeans_cluster(self):
        # First get the user tags data list
        tags_data = list(self.users_data["user_tags"])
        tags_data = [ast.literal_eval(item) for item in tags_data]
        tags_data = pd.DataFrame(tags_data)
        self.kmeans.fit(tags_data)
        return
    
    # Select n_closest nodes
    def select_n_closest(self, curr_id:int, num_closest:int=5) -> None:
        # Now get the cluster of the desired id
        cluster_map = pd.DataFrame()
        cluster_map = self.users_data
        # cluster_map['user_tag'] = self.users_data[""]
        cluster_map['cluster'] = self.kmeans.labels_
        id_cluster = cluster_map[cluster_map["user_id"] == curr_id]["cluster"].loc[0]
        self.curr_cluster = id_cluster
        # print(id_cluster)

        # Now have cluster, so we can filter 
        cluster_map = cluster_map[cluster_map["cluster"] == id_cluster]
        cluster_map = cluster_map[cluster_map["user_id"] != curr_id]
        # print(len(cluster_map))
        # Randomly sample from this dataframe
        cluster_map = cluster_map.sample(n=num_closest)
        # Just want the recommendations from this cluster
        history_lists = cluster_map["last_100"]
        history_lists = [ast.literal_eval(history) for history in history_lists]
        self.closest_histories = history_lists
        return 
    
    def get_items_to_queue(self, curr_id:int) -> list[int]:
        curr_id_row = self.users_data[self.users_data["user_id"] == curr_id].loc[0]
        curr_id_history = ast.literal_eval(curr_id_row["last_100"]).keys()
        # print(curr_id_history)
        MAX_SAMPLE = 2
        final_recommendations = []
        for history in self.closest_histories:
            curr_count = 0
            history_values = history.keys()
            for id in history_values:
                if not id in curr_id_history and not id in final_recommendations:
                    final_recommendations.append(id)
                    curr_count += 1
                if curr_count == MAX_SAMPLE:
                    break
        return final_recommendations
    
    def get_closest_companies(self) -> None:
        # First predict the cluster of the company
        for _, row in self.jobs_data.iterrows():
            curr_tag = pd.DataFrame(ast.literal_eval(row["company_tags"]), index=[0])
            cluster = self.kmeans.predict(curr_tag)
            if cluster == self.curr_cluster and row["company_id"] not in self.recommendations:
                print("SAME CLUSTER")
                self.recommendations.append(row["company_id"])
        return
    

    # Main function that collects all the recommendations
    def make_recommendations(self, user_id:int) -> None:
        self.create_kmeans_cluster()
        
        # User recommendations
        self.select_n_closest(user_id)
        self.recommendations += self.get_items_to_queue(user_id)
        print(recommender.recommendations)
        
        # Company recommendations
        self.get_closest_companies()
        print(recommender.recommendations)

        # Random Injections
        
        return
    
if __name__ == "__main__":
    recommender = RecommenderSystem()
    recommender.make_recommendations(0)