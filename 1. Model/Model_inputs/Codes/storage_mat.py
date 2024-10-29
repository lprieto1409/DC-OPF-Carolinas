# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:47:29 2023

@author: lprieto
"""

import pandas as pd
import numpy as np

# Folder
folder_model = '/Volumes/ElSoldeCusco/1. Research/18. 2nd paper/8. Github/M2S_extended/1. Model/Model_inputs/'

# Portfolios
Portfolios = ['P1', 'P2', 'P3']

# Loop over each portfolio
for portfolio in Portfolios:
    # Load data specific to each portfolio
    df = pd.read_csv(f"{folder_model}data_batparams_Interim_{portfolio}.csv", header=0)
    
    # Modify the 'node_bat' column values as per the original code
    for i in range(0, len(df)):
        df.loc[i, 'node_bat'] = 'n_' + str(df.loc[i, 'node_bat'])

    # Store the 'name' column in a variable
    store = df.loc[:, 'name']

    # Load the unique nodes file
    all_nodes = pd.read_csv(f"{folder_model}unique_nodes.csv", header=0, index_col=0)
    all_nodes.columns = ['Name']
    all_nodes = list(all_nodes['Name'])

    # Initialize the matrix A
    A = np.zeros((len(store), len(all_nodes)))
    df_A = pd.DataFrame(A)
    df_A.columns = all_nodes

    # List for missing nodes
    missing = []

    # Populate the matrix based on 'node_bat' presence in 'all_nodes'
    for i in range(0, len(store)):
        node = df.loc[i, 'node_bat']
        if node in all_nodes:
            df_A.loc[i, node] = 1
        else:
            missing.append(node)

    # Set the index of df_A to the 'name' column from df
    df_A.set_index(df['name'], inplace=True)

    # Save the matrix for each portfolio
    df_A.to_csv(f"{folder_model}storage_mat_Interim_{portfolio}.csv")

