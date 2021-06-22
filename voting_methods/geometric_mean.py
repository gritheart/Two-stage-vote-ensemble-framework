#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 21:34
# @Author  : kanyingxin
# @File    : geometric_mean.py
# @Software: PyCharm
# @Description: 
import pandas as pd
import math


def geometric_mean(df_results):
    # df for geometric mean
    colnames = list(df_results[0])
    df_mean_result = pd.DataFrame(index=list(df_results[0][colnames[0]]), columns=['score'])

    # calculate the geometric mean value for each gene
    # based on 5 results from every feature combined with 5 networks, respectively
    for iter, row in df_results[0].iterrows():
        product = float(1)
        gene = row[colnames[0]]
        # score of five netowrks
        for i in range(len(df_results)):
            colnames = list(df_results[i])
            x_name = colnames[1]
            product = product*df_results[i].loc[iter, x_name]
        # print('product: '+str(product))
        mean = math.pow(product, 1/5)
        # print('mean: '+str(mean))
        df_mean_result.loc[gene, 'score'] = mean

    return df_mean_result







