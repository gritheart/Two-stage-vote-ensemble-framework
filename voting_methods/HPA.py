#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 16:53
# @Author  : kanyingxin
# @File    : HPA.py
# @Software: PyCharm
# @Description:
import pandas as pd
from sklearn import preprocessing
import numpy as np
from utils.utils import Utils

#-*-coding:utf-8 -*-


def HPA_esembling(df_lst):
    colnames = list(df_lst[0])
    df_HPA_result = pd.DataFrame(index=list(df_lst[0][colnames[0]]), columns=['score'])
    # all_df_new = pd.DataFrame(index=list(df_result['gene_name']))

    # 1 get n rankings（n = end-start+1)
    rankings = []
    for i in range(len(df_lst)):
        colnames = list(df_lst[i])
        borda_df_value = df_lst[i][colnames[1]].tolist()
        # print(borda_df_value)
        sort_1 = sorted(enumerate(borda_df_value), key=lambda x: x[1])
        # print(sort_1)
        sort_2 = sorted(enumerate(sort_1), key=lambda x: x[1][0])
        # print(sort_2)
        borda_df_value_new = [i for i, v in sort_2]
        rankings.append(borda_df_value_new)
        # all_df_new[temp] = borda_df_value_new
    # print(rankings)

    # 2 calculate avg_ranking
    n = len(rankings)
    avg_ranking = [0] * len(rankings[0])
    rankings_normalized = preprocessing.normalize(rankings, norm='l2')
    # print(len(rankings_normalized))

    for i in range(n):
        # print(rankings_normalized[i])
        avg_ranking = avg_ranking + rankings[i]/(rankings_normalized[i]+0.000001)
    avg_ranking = 1/n * avg_ranking
    # print(avg_ranking)

    # 3 calculate the similarity of each ranking between avg_ranking
    sim = {}
    for i in range(n):
        sim_value = Utils.euclidean(avg_ranking, rankings[i])
        sim[i] = sim_value
    sim = dict(sorted(sim.items(),key=lambda d:d[1], reverse=False)) #false：ascending; true：descending
    # print(sim)

    # 4 calculate the weighted average ranking of TOP K most similar ranking with avg_ranking, K = 3
    k = 0
    final_ranking = np.zeros(len(df_lst[0][colnames[0]]))
    for key in sim.keys():
        k = k + 1
        if k > 3:
            break
        # print(key)
        # print(sim[key])
        final_ranking = final_ranking + sim[key] * np.array(rankings[key])
    final_ranking = list(final_ranking)
    # print(final_ranking)
    df_HPA_result['score'] = final_ranking


    return df_HPA_result










