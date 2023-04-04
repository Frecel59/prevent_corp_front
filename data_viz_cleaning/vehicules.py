import pandas as pd
import os

def df_clean_veh():
    directory = "data/raw_data/vehicules/1"

    files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]

    concatenated_veh1 = pd.DataFrame()
    for file in files:
        # Lecture du fichier CSV
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        # Concaténation avec le dataframe principal
        concatenated_veh_df1 = pd.concat([concatenated_veh1, df], ignore_index=True)

    directory = "data/raw_data/vehicules/2"

    files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]

    concatenated_veh2 = pd.DataFrame()
    for file in files:
        # Lecture du fichier CSV
        df2 = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        # Concaténation avec le dataframe principal
        concatenated_veh_df2 = pd.concat([concatenated_veh2, df2], ignore_index=True)

    df_veh = pd.concat([concatenated_veh_df1, concatenated_veh_df2], ignore_index=True)

    df_veh['type_vehicule'] = df_veh['catv'].replace({
        -1 :'2_roues',
        0 :'2_roues',
        1 : '2_roues',
        2 : '2_roues',
        3 : '2_roues',
        4 : '2_roues',
        5 : '2_roues',
        6 : '2_roues',
        7 : 'VL',
        8 : 'VL',
        9 : 'VL',
        10 : 'VL',
        11 : 'VL',
        12 : 'VL',
        13 : 'PL_TC',
        14 : 'PL_TC',
        15 : 'PL_TC',
        16 : 'PL_TC',
        17 : 'PL_TC',
        18 : 'PL_TC',
        19 : 'PL_TC',
        20 : 'PL_TC',
        21 : 'PL_TC',
        30 : '2_roues',
        31 : '2_roues',
        32 : '2_roues',
        33 : '2_roues',
        34 : '2_roues',
        35 : '2_roues',
        36 : '2_roues',
        37 : 'PL_TC',
        38 : 'PL_TC',
        39 : 'PL_TC',
        40 : 'PL_TC',
        41 : '2_roues',
        42 : '2_roues',
        43 : '2_roues',
        50 : '2_roues',
        60 : '2_roues',
        80 : '2_roues',
        99 : '2_roues'})

    df_veh.drop(columns=['senc', 'catv', 'occutc', 'obs', 'obsm', 'choc', \
        'manv', 'num_veh', 'id_vehicule', 'motor'], inplace=True)

    return df_veh


if __name__ == '__main__':
    df = df_clean_veh()
    # df.to_pickle("data/clean_data/clean_car.pickle")
    # df.to_pickle("data/clean_data/clean_car.tar")
    df.to_pickle("data/clean_data/clean_veh.gz")
    # df.to_csv("data/clean_data/clean_car.csv")
