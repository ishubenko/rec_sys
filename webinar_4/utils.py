import pandas as pd
import numpy as np


def prefilter_items(data, item_features, take_n_popular=5000):
    # Уберем самые популярные товары (их и так купят)
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
    
    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]
    
    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]
    
    # Уберем товары, которые не продавались за последние 12 месяцев
    items_without_sales_12_monts = data[data_train['week_no'] > (data_train['week_no'].max()-12)]
    data = data[~data['item_id'].isin(items_without_sales_12_monts)]
    
    # Уберем не интересные для рекоммендаций категории (department)
    #item_features = 
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    
    # Уберем слишком дорогие товарыs
    
    # ...
    k = take_n_popular -1
    data = data.loc[:k]
    
    return data
    
def postfilter_items(user_id, recommednations):
    pass