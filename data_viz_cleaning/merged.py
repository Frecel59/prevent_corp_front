import pandas as pd

from data_viz_cleaning.caracteristiques import df_clean_car
from data_viz_cleaning.lieux import df_clean_lie
from data_viz_cleaning.vehicules import df_clean_veh
from data_viz_cleaning.usagers import df_clean_usag


def merged_car_usag():
    df_car = pd.read_pickle("data/clean_data/clean_car.gz")
    df_usag = df_clean_usag()
    df_merged1 = pd.merge(df_car, df_usag, on='Num_Acc')

    df_merged1['lat'] = df_merged1['lat'].str.replace(',', '.').astype(float)
    df_merged1['long'] = df_merged1['long'].str.replace(',', '.').astype(float)

    return df_merged1


def merged_car_veh():
    df_car = pd.read_pickle("data/clean_data/clean_car.gz")
    df_veh = pd.read_pickle("data/clean_data/clean_veh.gz")
    df_merged2 = pd.merge(df_car, df_veh, on='Num_Acc')

    df_merged2['lat'] = df_merged2['lat'].str.replace(',', '.').astype(float)
    df_merged2['long'] = df_merged2['long'].str.replace(',', '.').astype(float)

    return df_merged2


def merged_car_lie():
    df_car = pd.read_pickle("data/clean_data/clean_car.gz")
    df_lie = df_clean_lie()
    df_merged3 = pd.merge(df_car, df_lie, on='Num_Acc')

    df_merged3['lat'] = df_merged3['lat'].str.replace(',', '.').astype(float)
    df_merged3['long'] = df_merged3['long'].str.replace(',', '.').astype(float)

    # Outliers

    mask = (df_merged3['long'] > 10) & (df_merged3['lat'] < 40)
    rows_to_drop = df_merged3[mask]

    df_merged3 = df_merged3.drop(rows_to_drop.index)

    return df_merged3
