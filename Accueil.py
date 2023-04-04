import streamlit as st
from PIL import Image
import pandas as pd

from data_viz_cleaning.caracteristiques import df_clean_car
from data_analysis_france import plot_acc_an, plot_acc_j_n, plot_acc_agglo, plot_acc_gravite, plot_acc_genre
from data_analysis_dep import plot_acc_an_dep, plot_acc_j_n_dep, plot_acc_agglo_dep, plot_acc_gravite_dep, plot_acc_genre_dep
from data_viz_cleaning.merged import merged_car_lie, merged_car_usag, merged_car_veh

# Définir la couleur de fond de la page
st.set_page_config(page_title="Prevent-Corp")



@st.cache_data
def load_df_car():
    # return df_clean_car()
    return pd.read_pickle("data/clean_data/clean_car.gz")

df_car = load_df_car()


@st.cache_data
def load_df_m_car_usag():
    return merged_car_usag()

df_merged1 = load_df_m_car_usag()


# Ajouter le CSS pour changer la couleur de fond
st.markdown(
    f"""
    <style>
        body, .stApp, .stApp > div > div {{
            background-color: #134f5c;
        }}
        .element-container .image-container .overlay {{
            display: none;
        }}
        .markdown-text-container, .stText, p, h1, h2, h3, h4, h5, h6, li {{
            color: #ffffff;
        }}
    </style>
    """, unsafe_allow_html=True
)


# Récupérer la valeur du choix à partir des paramètres de l'URL
query_params = st.experimental_get_query_params()
choice = query_params.get("choice", ["Accueil"])[0]

# Charger les images
logo1 = Image.open("img/logo_prevent_corp.png")

# Créer les colonnes pour centrer l'image
col1, col2, col3, col4, col5 = st.columns(5)

# Afficher l'image logo1 centrée sur la largeur de l'écran
col2.image(logo1, width=200)



# Créer la barre de navigation horizontale
menu = ["Accueil", "Visualisation", "Prédiction", "Suggestion", "L'équipe"]
st.markdown(
    f"""
    <style>
        .navbar {{
            overflow: hidden;
            display: flex;
        }}
        .navbar a {{
            margin-right: 10px;
            background-color: #ffd966ff;
            font-size: 18px;
            color: black;
            text-align: center;
            padding: 12px 16px;
            border: 1px solid black;
            border-radius: 5px;
            width: 200px;
            height: 50px;
        }}
        .navbar a:hover {{
            color: black;
        }}
        .navbar a.active {{
            color: white;
        }}
    </style>
    """
, unsafe_allow_html=True)

choice = __file__.split('/')[-1].split('.')[0].split('_')[-1]
link_format = lambda i, name: f'<a class="{"active" if choice==name else ""}" href="{name}" target="_self">{name}</a>'
menu_links = "".join([link_format(i, name) for i, name in enumerate(menu)])

st.markdown(f'<div class="navbar">{menu_links}</div>', unsafe_allow_html=True)

# Afficher la page sélectionnée


st.title("Bienvenu sur l'API de Prévent Corp")
st.subheader("Nous aidons les institutions à prévenir les accidents.")
st.write("Prevent-Corp est une plateforme conçue pour fournir des informations et des outils pour aider les institutions à prévenir les accidents. Notre objectif est de prédire les accidents à venir dans un département et à mettre en place des mesures préventives pour assurer la sécurité de la population.")

st.header("Nos services")
st.write("- Analyse des données d'accidents")
st.write("- Prédictions basées sur l'intelligence artificielle")
st.write("- Suggestions pour améliorer la sécurité")
st.write("- Assistance par une équipe d'experts")

st.header("Pour commencer")
st.write("**Affectation des ressources :** ")
st.write("Sur la base du nombre d’accidents prévu, les décideurs peuvent allouer des ressources telles que les services d’urgence, les forces de l’ordre et le personnel d’entretien aux États qui devraient connaître des taux d’accidents plus élevés.")

st.write("**Amélioration des infrastructures :** ")
st.write("Le modèle de prévision peut identifier les États susceptibles d’avoir plus d’accidents et les zones de ces États où les accidents sont les plus susceptibles de se produire. Ces informations peuvent être utilisées par les décideurs pour donner la priorité à l’amélioration des infrastructures telles que la réparation des routes, les feux de signalisation et les passages pour piétons dans ces zones.")

st.write("**Campagnes de sensibilisation du public :** ")
st.write("Les décideurs peuvent utiliser le nombre prévu d’accidents pour cibler les campagnes de sensibilisation du public dans les États où les taux d’accidents devraient être les plus élevés. Ces campagnes peuvent porter sur des questions telles que la conduite en état d’ivresse, la distraction au volant et le port de la ceinture de sécurité.")

st.write("**Taux d’assurance :** ")
st.write("Les compagnies d’assurance peuvent utiliser le nombre prévu d’accidents pour ajuster leurs tarifs en fonction des différents États. Si l’on s’attend à ce qu’un État ait un taux d’accidents plus élevé, les primes d’assurance pour les conducteurs de cet État peuvent être plus élevées que celles des autres États.")

st.write("**Planification du trafic :** ")
st.write("Le modèle de prévision peut aider les décideurs à planifier les embouteillages et les fermetures de routes dans les États où l’on s’attend à ce qu’il y ait plus d’accidents. Ces informations peuvent être utilisées pour développer des itinéraires alternatifs et des déviations afin de minimiser l’impact sur la circulation.")
