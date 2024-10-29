# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:47:29 2023

@author: lprieto
"""

import pandas as pd
import numpy as np

folder_model = '/Volumes/ElSoldeCusco/1. Research/18. 2nd paper/8. Github/M2S_extended/1. Model/Model_inputs/'

df = pd.read_csv(folder_model+'data_genparams_partial_corr.csv', header=0)
for i in range(0, len(df)):
    df.loc[i, 'node'] = 'n_' + str(df.loc[i, 'node'])

gens = df.loc[:, 'name']

all_nodes = pd.read_csv(folder_model+'unique_nodes_corr.csv', header=0, index_col=0)
all_nodes.columns = ['Name']
all_nodes = list(all_nodes['Name'])

A = np.zeros((len(gens), len(all_nodes)))

df_A = pd.DataFrame(A)
df_A.columns = all_nodes

missing = []

for i in range(0, len(gens)):
    node = df.loc[i, 'node']
    df_A.loc[i, node] = 1

    if node in all_nodes:
        pass
    else:
        missing.append(node)

df_A.set_index(df['name'], inplace=True)  # Setting the index to the 'name' column in df

df_A.to_csv(folder_model+'gen_mat_corr_2.csv')


