import pandas as pd
import os

def charac_clean_data_12_18():
    """ Fonction qui nettoies les données des années 2011 à 2018
        et retourne un data frame de toutes ces données
    """
    def update_format(dep):
        if dep > 90:
            dep = str(dep)
            return dep[:2]
        dep = str(dep)
        return dep[:1]
    directory = "data/raw_data/caracteristiques/1"
    files = [file for file in os.listdir(directory) if file.startswith("caracteristiques_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)
    data = data.drop(columns=["jour", "hrmn", "com", "adr", "gps", "col", "int"])
    data["dep"] = data["dep"].apply(update_format)
    data = data.astype({'dep': int})
    deps_to_delete = [971, 972, 973, 974, 976, 201, 202, 97]
    data = data.drop(data[data['dep'].isin(deps_to_delete)].index)
    print("Cleaning Caractéristique de 2012 à 2018 -> Done")
    return data

def charac_clean_data_19_21():
    """ Fonction qui nettoies les données des années 2019 à 2021
        et retourne un data frame de toutes ces données
    """
    print("Cleaning Characteristics de 2019 à 2021 ...")
    directory = "data/raw_data/caracteristiques/2"
    files = [file for file in os.listdir(directory) if file.startswith("caracteristiques_") and file.endswith(".csv")]
    data = pd.DataFrame()

    for file in files:
        df2 = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df2], ignore_index=True)

    data = data.drop(columns=["jour", "hrmn", "com", "adr", "int", "col"])
    deps_to_delete = ["972", "2B", "973", "2A", "987", "986", "971", "977", "978", "975", "988", "976", "974" ]
    data = data.drop(data[data['dep'].isin(deps_to_delete)].index)
    data = data.astype({'dep': int})
    print("Cleaning Characteristics de 2019 à 2021 -> Done")
    return data

def concatenate_function(name, data_1 :pd.DataFrame, data_2 :pd.DataFrame) -> pd.DataFrame:
    """ Fusionne les deux data fram de caracéristique et retourne le
        data farm avec les accidents dans lo'dre d'arrivé
    """
    print(f"Fusion des Dataframe {name} 2011-2018 et 2019-2021 ...")
    return pd.concat([data_1, data_2], ignore_index=True).sort_values(by="Num_Acc")

def df_clean_car():
    df_car = concatenate_function("Characteristics", charac_clean_data_12_18(), charac_clean_data_19_21())

    df_car['conditon_meteo'] = df_car['atm'].replace({
        -1: 'perturbation',
        1 : 'normal',
        2 : 'perturbation',
        3 : 'perturbation',
        4 : 'perturbation',
        5 : 'perturbation',
        6 : 'perturbation',
        7 : 'perturbation',
        8 : 'perturbation',
        9 : 'perturbation'
    })

    df_car['zone'] = df_car['agg'].replace({
        1 : 'hors_agglomeration',
        2 : 'agglomeration',
    })

    df_car['heure'] = df_car['lum'].replace({
        1 : 'jour',
        2 : 'jour',
        3 : 'nuit',
        4 : 'nuit',
        5 : 'nuit',
        -1: 'nuit'
    })

    df_car.drop(columns=['atm', 'agg', 'lum'], inplace=True)

    df_car['an'] = df_car['an'].replace({
        11: 2011,
        12: 2012,
        13: 2013,
        14: 2014,
        15: 2015,
        16: 2016,
        17: 2017,
        18: 2018,
    })

    df_car['date'] = pd.to_datetime(df_car['an'].astype(str) + '-' + df_car['mois'].astype(str), format='%Y-%m')

    df_car.drop(['an', 'mois'], axis=1, inplace=True)

    return df_car

if __name__ == '__main__':
    df = df_clean_car()
    # df.to_pickle("data/clean_data/clean_car.pickle")
    # df.to_pickle("data/clean_data/clean_car.tar")
    df.to_pickle("data/clean_data/clean_car.gz")
    # df.to_csv("data/clean_data/clean_car.csv")
