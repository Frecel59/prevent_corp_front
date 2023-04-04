import matplotlib.pyplot as plt
import seaborn as sns

from data_viz_cleaning.merged import merged_car_lie
from data_viz_cleaning.merged import merged_car_usag
from data_viz_cleaning.merged import merged_car_veh
from data_viz_cleaning.caracteristiques import df_clean_car

def plot_acc_an(df_car):
    # df_car = df_clean_car()
    sns.set_style('darkgrid')
    sns.set_palette('Set2')
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

def plot_acc_gravite(df_merged1):
    plt.figure(figsize=(7,6))
    sns.scatterplot(x='long', y='lat', data=df_merged1, hue='gravité', palette='husl')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Location des accidents classés par gravité')

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
