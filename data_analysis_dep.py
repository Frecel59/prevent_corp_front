import matplotlib.pyplot as plt
import seaborn as sns

from data_viz_cleaning.merged import merged_car_lie
from data_viz_cleaning.merged import merged_car_usag
from data_viz_cleaning.merged import merged_car_veh
from data_viz_cleaning.caracteristiques import df_clean_car

def plot_acc_an_dep(df_car, input_dep):

    # Créer une nouvelle colonne pour l'année
    df_car['year'] = df_car['date'].dt.year

    # Filtrer les données pour le département
    df_car_dep = df_car[df_car['dep'] == input_dep]

    # Tracer le graphique
    sns.set_style('darkgrid')
    sns.set_palette('Set2')
    plt.figure(figsize=(6,4))
    sns.countplot(x='year', data=df_car_dep)
    plt.title(f"Nombre d'accidents par an pour le département {input_dep}")
    plt.xlabel('Année')
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_j_n_dep(df_car, input_dep):

    # Filtrer les données pour le département
    df_car_dep = df_car[df_car['dep'] == input_dep]

    # Tracer le graphique
    plt.figure(figsize=(8,6))
    palette = ["lightskyblue", "navy"]
    sns.countplot(x='heure', data=df_car_dep, order=df_car_dep['heure'].value_counts().index, palette=palette)
    plt.title(f"Nombre d'accidents : jour / nuit pour le département {input_dep}")
    plt.xlabel("Heure de la journée")
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_agglo_dep(df_car, input_dep):

    # Filtrer les données pour le département
    df_car_dep = df_car[df_car['dep'] == input_dep]

    plt.figure(figsize=(8,6))
    sns.countplot(x='zone', data=df_car_dep, hue='conditon_meteo', palette='Set2')
    plt.title(f"Nombre d'accidents par zone pour le département {input_dep}")
    plt.xlabel('Zone')
    plt.ylabel("Nombre d'accidents")

    return plt

def plot_acc_type_dep(df_merged1, input_dep):
    df_merged1_dep = df_merged1[df_merged1['dep'] == input_dep]
    # créer une liste de couleurs personnalisée
    couleurs = ['#F9A729', '#56B4E9', '#009E73']

    # tracer le graphique avec la nouvelle palette de couleurs
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df_merged1_dep, x='catégorie', palette=couleurs)
    plt.ylabel("Nombre d'accidentés")
    plt.title(f"Répartition des accidents par type d'individu pour le département {input_dep}")

    return plt

def plot_acc_gravite_dep(df_merged1, input_dep):

    # Filtrer les données pour le département
    df_merged1_dep = df_merged1[df_merged1['dep'] == input_dep]

    plt.figure(figsize=(7,6))
    sns.scatterplot(x='long', y='lat', data=df_merged1_dep, hue='gravité')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f"Localisation des accidents par gravité pour le département {input_dep}")

    return plt

def plot_acc_genre_dep(df_merged1, input_dep):

    # Filtrer les données pour le département
    df_merged1_dep = df_merged1[df_merged1['dep'] == input_dep]

    plt.figure(figsize=(7,6))
    gender_count = df_merged1_dep['sexe'].value_counts()
    labels = ['Homme', 'Femme']
    colors = ['cornflowerblue', 'lightcoral']
    plt.pie(gender_count, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title(f"Accidents par genre pour le département {input_dep}")
    plt.axis('equal')

    return plt

def plot_acc_type_veh_dep(df_merged2, input_dep):
    df_merged2 = df_merged2.drop(df_merged2[df_merged2['long'] > 10].index)
    df_merged2_dep = df_merged2[df_merged2['dep'] == input_dep]

    plt.figure(figsize=(7,6))
    sns.scatterplot(x='long', y='lat', data=df_merged2_dep, hue='type_vehicule', palette='husl')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'Localisation par type de véhicule pour le département {input_dep}')
    sns.set_style("whitegrid")

    return plt

def plot_acc_route_meteo_dep(df_merged3, input_dep):
    df_merged3_dep = df_merged3[df_merged3['dep'] == input_dep]

    sns.countplot(x='type_route', data=df_merged3_dep, hue='etat_surface')
    plt.xlabel('Type de route')
    plt.ylabel('Nombre accidents')
    plt.title(f'Répartition par type de route et condition météo pour le département {input_dep}')
    plt.legend(title='Condition météo')
    sns.set_style("ticks")

    return plt
