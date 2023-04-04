import pandas as pd
import os

def df_clean_lie():
    df_lie1 = pd.read_csv("data/clean_data/lieux1_concat.csv")
    df_lie2 = pd.read_csv("data/clean_data/lieux2_concat2.csv")
    df_lie = pd.concat([df_lie1, df_lie2], ignore_index=True)

    df_lie['type_route'] = df_lie['catr'].replace({
    1: 'autoroute',
    2: 'route',
    3: 'route',
    4: 'voie',
    5: 'voie',
    6: 'voie',
    7: 'route',
    9: 'voie'})

    df_lie['etat_surface'] = df_lie['surf'].replace({
    -1:'autre',
    0:'autre',
    1: 'sèche',
    2: 'humide/gelée',
    3: 'humide/gelée',
    4: 'humide/gelée',
    5: 'humide/gelée',
    6: 'humide/gelée',
    7: 'humide/gelée',
    8:'autre',
    9:'autre'})

    df_lie.drop(columns=['lartpc', 'larrout', 'v1' , 'v2', 'voie', 'env1', \
        'vma', 'catr', 'circ', 'nbv', 'surf', 'infra', 'pr', 'pr1', 'vosp', \
        'prof', 'plan', 'situ'], inplace=True)

    return df_lie
