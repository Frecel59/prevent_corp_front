import pandas as pd
import os
import datetime

def df_clean_usag():
    df_usag1 = pd.read_csv("data/clean_data/usagers1_concat.csv")
    df_usag2 = pd.read_csv("data/clean_data/usagers2_concat2.csv")
    df_usag = pd.concat([df_usag1, df_usag2], ignore_index=True)

    df_usag = df_usag.drop_duplicates()

    df_usag.drop(columns=['id_vehicule', 'secu1', 'secu2', 'secu3'], inplace=True)

    df_usag['gravité'] = df_usag['grav'].replace({
    -1: 'indemne',
    1: 'indemne',
    2: 'mort',
    3: 'blessé',
    4: 'blessé'})

    date_actuelle = datetime.datetime.now().year
    df_usag['age'] = df_usag['an_nais'].apply(lambda x: date_actuelle - x)

    df_usag['sexe'] = df_usag['sexe'].replace({1: 'homme', 2: 'femme'})
    df_usag['sexe'] = df_usag['sexe'].replace({-1: 'homme'})

    df_usag['catégorie'] = df_usag['catu'].replace({
    1: 'conducteur',
    2: 'passager',
    3: 'piéton',
    4: 'conducteur'})

    df_usag['trajet'] = df_usag['trajet'].replace({
    -1:'autre',
    0: 'autre',
    1: 'domicile',
    2: 'domicile',
    3: 'domicile',
    4: 'travail',
    5: 'loisir' ,
    9: 'loisir'})

    df_usag.drop(columns=['num_veh', 'locp', 'place', 'etatp', 'actp', 'secu', 'an_nais', 'grav', 'catu'], inplace=True)

    return df_usag
