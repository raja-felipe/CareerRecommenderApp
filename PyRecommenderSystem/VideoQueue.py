from RecommenderSystem import RecommenderSystem
import os
import sys

# Determine the directory of your Python files
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory to the system path
sys.path.append(current_dir)

QUEUE_MAX = 10
THRESHOLD_ADD = 2

class VideoQueueManager():
    path_to_folder : str
    recommender : RecommenderSystem

    def __init__(self):
        self.recommender = RecommenderSystem()
        return
    
    def check_threshold(self) -> bool:
        return len(os.listdir(self.path_to_folder)) <= 2
    
    def refill_queue(self) -> None:
        if self.check_threshold():
            self.recommender.make_recommendations()
            # Now re-map the recommendations back to the video files
        return