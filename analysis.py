import pandas as pd
import numpy as np
from statistics import mean, stdev
from scipy import stats

rankings_df = pd.read_csv('./data/b1g_data.csv')


def standardize(col,reverse):
    mx = max(col)
    mn = min(col)
    r = mx - mn
    if reverse:
        l = [((mx - x) / r) * 100 for x in col]
    else:
        l = [((x-mn) / r) * 100 for x in col]

    return l



def mean(data):
    ranking_cols = [c for c in data.columns if
                    c in ['bpi_score', 'pomeory_score', 'sagarin_score', 'moore_score', 'lrmc_score', 'pre_seed_score',
                          'big_seed_score']]
    new_df = data[ranking_cols]
    data['mean_score'] = new_df.apply(lambda x: x.mean(), axis=1)
    return data[['Team', 'big_seed', 'mean_score', 'need_to_win']]


def final(x):
    score = x['mean_score']
    if x['need_to_win'] == 1:
        score += 2.25
    elif x['need_to_win'] == 2:
        score += 1.75
    elif x['need_to_win'] == 3:
        score += 1.25
    if x['big_seed'] <= 4:
        score += 1.75
    elif x['big_seed'] <= 6:
        score += 1
    return score


rank_cols = [c for c in rankings_df.columns if c not in ['Team']]
for col in rank_cols:
    new_col_name = f'{col}_score'
    col_list = list(rankings_df[col])
    rankings_df[new_col_name] = standardize(col_list, reverse = True)

new_data = mean(rankings_df)
new_data['final_score'] = new_data.apply(lambda x: final(x), axis=1)

new_data.to_csv('./data/b1g_ratings.csv', index=False)


