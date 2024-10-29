# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:47:29 2023

@author: lprieto
"""

import pandas as pd
import numpy as np

folder_model = '/Volumes/ElSoldeCusco/1. Research/18. 2nd paper/8. Github/M2S_extended/1. Model/Model_inputs/'

# Portfolios
Portfolios = ['P1', 'P2', 'P3']

# Load all nodes
all_nodes = pd.read_csv(folder_model + 'unique_nodes.csv', header=0, index_col=0)
all_nodes.columns = ['Name']
all_nodes = list(all_nodes['Name'])

for portfolio in Portfolios:
    # Load the specific portfolio's data
    df = pd.read_csv(f"{folder_model}data_genparams_partial_Interim_{portfolio}.csv", header=0)
    
    # Update node column to include 'n_' prefix
    df['node'] = df['node'].apply(lambda x: 'n_' + str(x))
    gens = df['name']

    # Initialize empty matrix
    A = np.zeros((len(gens), len(all_nodes)))

    # Create DataFrame for matrix with all nodes as columns
    df_A = pd.DataFrame(A, columns=all_nodes)

    # Track missing nodes
    missing = []

    for i, node in enumerate(df['node']):
        if node in all_nodes:
            df_A.loc[i, node] = 1
        else:
            missing.append(node)

    # Set index to generator names
    df_A.set_index(gens, inplace=True)

    # Save the matrix to a CSV file specific to each portfolio
    df_A.to_csv(f"{folder_model}gen_mat_Interim_{portfolio}.csv")

    # Print any missing nodes for debugging if needed
    if missing:
        print(f"Missing nodes for portfolio {portfolio}: {missing}")
