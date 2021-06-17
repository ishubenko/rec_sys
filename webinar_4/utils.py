import pandas as pd
import numpy as np


def prefilter_items(data, item_features, take_n_popular=1000):
    # Уберем самые популярные товары (их и так купят)
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() #/ data_train['user_id'].nunique()
    popularity['user_id'] = popularity['user_id'] / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
    
    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]
    
    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.0005].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]
    
    # Уберем товары, которые не продавались за последние 12 месяцев
    items_without_sales_12_monts = data[data['week_no'] > (data['week_no'].max()-52)] # 52 недели в году
    data = data[~data['item_id'].isin(items_without_sales_12_monts)]
    
    # Уберем не интересные для рекоммендаций категории (department)
    
    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб. 
    
    # Уберем слишком дорогие товары
    
    # ...
    
    # Выбираем k популярных товаров из оставшихся
    n = take_n_popular -1
    # Еще раз выбираем самые популярные
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() #/ data_train['user_id'].nunique()
    popularity['user_id'] = popularity['user_id'] / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
    # сОРТИРУЕМ по созданному признаку
    sorted_n_popular = popularity.sort_values(by='share_unique_users', ascending=False)
    top_n = sorted_n_popular.iloc[:take_n_popular]
    # Выбираем k популярных и записываем в data
    #data = data[data['item_id'].isin(sorted_n_popular.loc[:k])]
    data = data[data['item_id'].isin(top_n['item_id'])]
    
    return data
    
def postfilter_items(user_id, recommednations):
    pass