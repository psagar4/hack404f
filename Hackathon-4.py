
# coding: utf-8

# In[33]:


import pandas as pd
from surprise.model_selection import train_test_split
from surprise import Dataset                                                     
from surprise import Reader 
from surprise.accuracy import rmse
from surprise.model_selection import cross_validate
from surprise import SVD
from surprise import KNNBasic


# In[3]:


ratings = pd.read_csv("Desktop/Hackathon/final_rating.csv")


# In[4]:


data = pd.read_csv("Desktop/Hackathon/final_rating.csv")


# In[44]:


algo_svd = SVD()
reader = Reader(rating_scale=(0, 5))
data = Dataset.load_from_df(ratings,reader)


# In[45]:


trainset, testset = train_test_split(data, test_size=0.2)


# In[46]:


algo_svd.fit(trainset)                             
predictions_svd = algo_svd.test(testset)


# In[58]:


def user_prediction(user_id,credit_id):
    pred = 0
    for i in predictions_svd:
        if i.uid == user_id and i.iid == credit_id:
            pred = i.est
            break
    return pred

