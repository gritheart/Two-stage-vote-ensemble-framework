#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 21:34
# @Author  : kanyingxin
# @File    : borda_voting.py
# @Software: PyCharm
# @Description: what for


import pandas as pd
import numpy as np



def borda_voting(df_results):
    # df for borda
    colnames = list(df_results[0])
    df_borda_result = pd.DataFrame(index=list(df_results[0][colnames[0]]), columns=['score'])

    all_df_new = pd.DataFrame(index=list(df_results[0][colnames[0]]))

    # get a new df by deal with all dfs from df_results
    # rank genes according to the scores of each network
    for i in range(len(df_results)):
        colnames = list(df_results[i])
        x_name = colnames[1]
        borda_df_value = df_results[i][x_name].tolist()
        # print(borda_df_value)
        sort_1 = sorted(enumerate(borda_df_value), key=lambda x: x[1])
        # print(sort_1)
        sort_2 = sorted(enumerate(sort_1), key=lambda x: x[1][0])  # ascending, higher scores with bigger ranking
        # print(sort_2)
        borda_df_value_new = [i for i, v in sort_2]
        all_df_new[x_name] = borda_df_value_new
        # break
    # print(all_df_new.head())

    for iter, row in all_df_new.iterrows():
        score = np.mean(list(row))
        df_borda_result.loc[iter, 'score'] = score

    return df_borda_result
