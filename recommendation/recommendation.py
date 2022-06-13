from simirarity import item_simirarity  as ism
from simirarity import user_simirarity as usm
from simirarity.import_data import database
import pandas as pd
from collections import defaultdict

def recommendation(user, data, clothes):
    
    clothes_columns = ['clothesId', 'fit', 'closet_color', 'closet_style', 'spring', 'summer', 'autumn', 'winter', 'subCategory', 'mainCategory']
    prefrence_columns = ['userId_id', 'codiId_id']
    codi_clothes_columns = ['codiId', 'clothesId_id']
    
    clothes_data = pd.DataFrame(data[0], columns=clothes_columns)
    preference_data = pd.DataFrame(data[1], columns=prefrence_columns)
    codi_clothes_data = pd.DataFrame(data[2], columns=codi_clothes_columns)
    #user_columns = []
    user_data = pd.DataFrame([list(clothes.values())], columns=clothes_columns)
    clothes_data = pd.concat([clothes_data, user_data])
    
    recommand_codies = usm.find_nearest_users(preference_data, user)
    clothes_data = clothes_data.set_index('clothesId', drop=False)
    codi_clothes_data = codi_clothes_data.set_index('codiId', drop=False)
    recommand_codi_clothes_data = pd.DataFrame(columns = codi_clothes_data.columns)
    for codi in recommand_codies:
        try:
            recommand_codi_clothes_data = pd.concat([recommand_codi_clothes_data, codi_clothes_data.loc[codi]])
        except:
            continue
    codi_clotes_dict = defaultdict(list)
    
    for i in range(len(codi_clothes_data)):
        data = codi_clothes_data.iloc[i].values
        codi_clotes_dict[data[0]].append(data[1])
    
    for codi in codi_clotes_dict.keys():
        category = clothes_data.loc[codi_clotes_dict[codi][0]]['mainCategory']
        if  category == '스커트' or category == '바지':
            codi_clotes_dict[codi][0], codi_clotes_dict[codi][1] = codi_clotes_dict[codi][1], codi_clotes_dict[codi][0]
    
    clothes_dict = defaultdict(int)
#     #item = 580958
    category = clothes_data.loc[clothes['clothesId']]['mainCategory']
    candidates = [clothes['clothesId']]
    if category == '스커트' or category == '바지':
        category_idx, recommand_idx = 1, 0
    else:
        category_idx, recommand_idx = 0, 1
    for item in codi_clotes_dict.values():
        clothes_dict[item[category_idx]] = item[recommand_idx]
        candidates.append(item[category_idx])

    #print(candidates)
    candidates_data = clothes_data.loc[candidates]

    recommandations = ism.genre_recommendations(clothes['clothesId'], candidates_data, clothes_columns)
    recommandations = [clothes_dict[item] for item in recommandations]

    return recommandations



