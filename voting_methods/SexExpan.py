#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 10:19
# @Author  : kanyingxin
# @File    : SexExpan.py
# @Software: PyCharm
# @Description:

import pandas as pd


def sexExpan(df_results):
    colnames = list(df_results[0])
    df_sexExpan_result = pd.DataFrame(index=list(df_results[0][colnames[0]]), columns=['score'])

    # 1 get n rankings（n = end-start+1)
    rankings = []
    for i in range(len(df_results)):
        colnames = list(df_results[i])
        x_name = colnames[1]
        borda_df_value = df_results[i][x_name].tolist()
        # print(borda_df_value)
        sort_1 = sorted(enumerate(borda_df_value), key=lambda x: x[1])
        # print(sort_1)
        sort_2 = sorted(enumerate(sort_1), key=lambda x: x[1][0])
        # print(sort_2)
        borda_df_value_new = [i for i, v in sort_2]
        rankings.append(borda_df_value_new)
        # all_df_new[temp] = borda_df_value_new
    # print(rankings)

    # 2 calculate mrr score for each gene
    mrr = {}
    for iter, row in df_results[0].iterrows():
        gene = row[0]
        mrr[gene] = 0
        for i in range(len(rankings)):
            mrr[gene] = mrr[gene] + 1/(rankings[i][iter]+1)

    # 3 sort gene by mrr score, and then return df
    for key in mrr.keys():
        df_sexExpan_result.loc[key, 'score'] = mrr[key]
    # print(df_sexExpan_result)

    # df_save = df_sexExpan_result.sort_index()
    # save_path = 'document/csv/voting_result/' + cancer + '/' + vector
    # isExist = os.path.exists(save_path)
    # if not isExist:
    #     os.makedirs(save_path)
    # df_save.to_csv(save_path + '/' + cancer + '_SexExpan.csv')

    return df_sexExpan_result


