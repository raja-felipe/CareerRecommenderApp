from RecommenderSystem import RecommenderSystem
from DataGenerator import JOB_SAVE_PATH, VIDEO_STORE_FOLDER, VIDEO_QUEUE_FOLDER
import os
import sys
import pandas as pd
import shutil
import time

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

QUEUE_MAX = 5
THRESHOLD_ADD = 2

class VideoQueueManager():
    path_to_source: str
    path_to_queue : str
    recommender : RecommenderSystem

    def __init__(self, path_to_queue:str=VIDEO_QUEUE_FOLDER, path_to_source:str = VIDEO_STORE_FOLDER):
        self.recommender = RecommenderSystem()
        self.path_to_source = path_to_source
        self.path_to_queue = path_to_queue
        return
    
    def check_threshold(self) -> bool:
        return len(os.listdir(self.path_to_queue)) <= 2
    
    def refill_queue(self, user_id:int) -> None:
        if self.check_threshold():
            self.recommender.make_recommendations(user_id)

            # Now re-map the recommendations back to the video files
            company_data = pd.read_csv(JOB_SAVE_PATH)
            num_in_queue = 0
            for company_id in self.recommender.recommendations:
                # Filter out only the relative path of the file
                src_path = company_data[company_data["company_id"] == company_id]["video_location"].values[0]
                video_name = src_path[len(self.path_to_source):]
                if video_name not in os.listdir(self.path_to_queue):
                    # Add the video to the folder
                    to_add_path = self.path_to_queue + video_name
                    # Adjust the paths
                    # src_path = src_path.replace("\\", "/")
                    # to_add_path = to_add_path.replace("\\", "/")
                    shutil.copy2(src_path, to_add_path)
                    num_in_queue += 1
                    if num_in_queue == QUEUE_MAX:
                        break
        return
    
def main(manager: VideoQueueManager, user_id:int = 0):
    TIME_TO_CHECK = 180
    start_time = time.time()

    while True:
        if time.time() - start_time >= TIME_TO_CHECK:
            manager.refill_queue(user_id)
            start_time = time.time()


if __name__ == "__main__":
    manager = VideoQueueManager()
    # manager.refill_queue()
    main(manager)