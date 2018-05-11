from django.apps import AppConfig

import pandas as pd

from surprise.model_selection import train_test_split
from surprise import Dataset                                                     
from surprise import Reader 
from surprise.accuracy import rmse
from surprise.model_selection import cross_validate
from surprise import SVD
from surprise import KNNBasic

import os

class ServerConfig(AppConfig):
    name = 'server'
    algo_svd = SVD()
    
    def ready(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ratings = pd.read_csv(os.path.join(BASE_DIR, 'rating_comp.csv'))
        data = Dataset.load_from_df(ratings, Reader())
        #self.trainset, self.testset = train_test_split(data, test_size=0.25)
        self.trainset = data.build_full_trainset()
        self.algo_svd.fit(self.trainset)
        #predictions_svd = self.algo_svd.test(self.testset)
        print("Server up!")