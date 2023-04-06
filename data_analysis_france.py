import matplotlib.pyplot as plt
import seaborn as sns

from data_viz_cleaning.merged import merged_car_lie
from data_viz_cleaning.merged import merged_car_usag
from data_viz_cleaning.merged import merged_car_veh
from data_viz_cleaning.caracteristiques import df_clean_car

def plot_acc_an(df_car):
    # df_car = df_clean_car()
    sns.set_style('darkgrid')
    sns.set_palette('Set3')
    plt.figure(figsize=(8,6))
    sns.countplot(x=df_car['date'].dt.year)
    plt.title("Nombre d'accidents par an")
    plt.xlabel('Année')
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_j_n(df_car):
    plt.figure(figsize=(8,6))
    palette = ["lightskyblue", "navy"]
    sns.countplot(x='heure', data=df_car, order=df_car['heure'].value_counts().index, palette=palette)
    plt.title("Nombre d'accidents : jour / nuit")
    plt.xlabel("Heure de la journée")
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_agglo(df_car):
    plt.figure(figsize=(8,6))
    sns.countplot(x='zone', data=df_car, hue='conditon_meteo', palette='Set2')
    plt.title("Nombre d'accidents par zone")
    plt.xlabel('Zone')
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_type(df_merged1):
    # créer une liste de couleurs personnalisée
    couleurs = ['#F9A729', '#56B4E9', '#009E73']

    # tracer le graphique avec la nouvelle palette de couleurs
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df_merged1, x='catégorie', palette=couleurs)
    plt.ylabel("Nombre d'accidentés")
    plt.title("Répartition des accidents par type d'individu")

    return plt

def plot_acc_gravite(df_merged1):
    plt.figure(figsize=(7,6))
    sns.scatterplot(x='long', y='lat', data=df_merged1, hue='gravité', palette='husl')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Localisation des accidents par gravité')

    return plt

def plot_acc_genre(df_merged1):
    plt.figure(figsize=(7,6))
    gender_count = df_merged1['sexe'].value_counts()
    labels = ['Homme', 'Femme']
    colors = ['cornflowerblue', 'lightcoral']
    plt.pie(gender_count, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Accidents par genre')
    plt.axis('equal')

    return plt

def plot_acc_type_veh(df_merged2):
    df_merged2 = df_merged2.drop(df_merged2[df_merged2['long'] > 10].index)

    plt.figure(figsize=(7,6))
    sns.scatterplot(x='long', y='lat', data=df_merged2, hue='type_vehicule', palette='husl')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Localisation par type de véhicule')
    sns.set_style("whitegrid")

    return plt

def plot_acc_route_meteo(df_merged3):
    sns.countplot(x='type_route', data=df_merged3, hue='etat_surface')
    plt.xlabel('Type de route')
    plt.ylabel('Nombre accidents')
    plt.title('Répartition par type de route et condition météo')
    plt.legend(title='Condition météo')
    sns.set_style("ticks")

    return plt
