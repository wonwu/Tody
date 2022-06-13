import math
import numpy as np
from numpy import linalg as LA
import pandas as pd
from random import randint
from sklearn.metrics.pairwise import cosine_similarity
pd.options.mode.chained_assignment = None 
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict



def selection_to_rating(data):
    codi_user_dict = defaultdict(list)
    selected = []
    user_codi_dict = defaultdict(list)
    for i in range(len(data)):
        codi = data.iloc[i]['codiId_id']
        user = data.iloc[i]['userId_id']
#         rating = data.iloc[i]['rating']
#         if rating:
#             codi_user_dict[codi].append(user)
        codi_user_dict[codi].append(user)
        user_codi_dict[user].append(codi)
    
    for codi in codi_user_dict.keys():
        for user in data['userId_id'].unique():
            if user in codi_user_dict[codi]:
                selected.append((user, codi, 1))
            else:
                selected.append((user, codi, 0))
    rating_df = pd.DataFrame(selected, columns = ['userId_id', 'codiId_id', 'rating'])
    return rating_df, user_codi_dict


def user_link(data, user, k=5):
    a=data.pivot_table('rating', index='userId_id', columns='codiId_id')
    ratings_matrix_T=a.T
    ratings_matrix=a
    item_sim = cosine_similarity(ratings_matrix,ratings_matrix)  
    item_sim_df = pd.DataFrame(data=item_sim, index=ratings_matrix_T.columns, # 코사인유사도로 변환된 넘파이 행렬을 유저를 매핑하여 dataframe으로 변환
                              columns=ratings_matrix_T.columns)
    userlink=item_sim_df.loc[user].sort_values(ascending=False)[:k]
    return list(userlink.index)


def find_nearest_users(data, user, k=5):
    rating_df, user_codi_dict = selection_to_rating(data)
    userlink = user_link(rating_df, user, k)
    recomand_codies = set()
    for user in userlink:
        for codi in user_codi_dict[user]:
            recomand_codies.add(codi)
    return list(recomand_codies)
