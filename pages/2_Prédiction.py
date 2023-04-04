import streamlit as st
from PIL import Image
import pandas as pd

from data_viz_cleaning.caracteristiques import df_clean_car
from data_analysis_dep import plot_acc_an_dep, plot_acc_j_n_dep, \
    plot_acc_agglo_dep, plot_acc_gravite_dep, plot_acc_genre_dep, \
    plot_acc_type_dep, plot_acc_type_veh_dep, plot_acc_route_meteo_dep
from data_viz_cleaning.merged import merged_car_lie, merged_car_usag, merged_car_veh

# Définir la couleur de fond de la page
st.set_page_config(page_title="Prevent-Corp", initial_sidebar_state="collapsed")



@st.cache_data
def load_df_car():
    # return df_clean_car()
    return pd.read_pickle("data/clean_data/clean_car.gz")

df_car = load_df_car()


@st.cache_data
def load_df_m_car_usag():
    return merged_car_usag()

df_merged1 = load_df_m_car_usag()

@st.cache_data
def load_df_m_car_veh():
    return merged_car_veh()

df_merged2 = load_df_m_car_veh()

@st.cache_data
def load_df_m_car_lie():
    return merged_car_lie()

df_merged3 = load_df_m_car_lie()

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
            text-decoration: none;
        }}
        .navbar a:hover {{
            color: black;
            text-decoration: underline;
        }}
        .navbar a.active {{
            color: #134f5c;
            font-weight: bold;
            text-decoration: none;
        }}
    </style>
    """
, unsafe_allow_html=True)



choice = __file__.split('/')[-1].split('.')[0].split('_')[-1]
link_format = lambda i, name: f'<a class="{"active" if choice==name else ""}" \
    href="{name}" target="_self">{name}</a>'
menu_links = "".join([link_format(i, name) for i, name in enumerate(menu)])

st.markdown(f'<div class="navbar">{menu_links}</div>', unsafe_allow_html=True)

# Afficher la page sélectionnée


st.title("Prédiction d'un département !")
st.write("Pour ce projet, nous ne disposions pas de suffissament de données \
    pour proposer des prédictions sur les départements hors france métropolitaine")

input_dep = st.number_input("Entrez le numéro du département (1 à 95) :", \
    value=75, min_value=1, max_value=95)

st.write(f"<h3 style='text-align: center; font-size: 25px;'>Prédiction du \
    nombre d'accident pour le département | {input_dep} |</h3>", \
        unsafe_allow_html=True)
st.write("En attente...")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.write(f"<h3 style='text-align: center; font-size: 25px;'>Statistiques des 10 \
    dernières années pour le département | {input_dep} |</h3>", \
        unsafe_allow_html=True)

# st.pyplot(plot_acc_an_dep(df_car, input_dep))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_j_n_dep(df_car, input_dep))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_agglo_dep(df_car, input_dep))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_gravite_dep(df_merged1, input_dep))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_genre_dep(df_merged1, input_dep))
# st.markdown("<br>", unsafe_allow_html=True)

# Liste des noms des plots
plot_names = ['Nbr accidents', 'Répartition jour / nuit', 'Agglo / hors agglo', \
    "Répartition par type d'individu", 'Répartition de la gravité', \
    'Répartition par genre', 'Localisation par type de véhicule', 'Répartition \
    par type de route et condition météo']

# Menu déroulant pour sélectionner le plot
selected_plot = st.selectbox('Sélectionnez un graph à afficher', plot_names)

# Affichage du plot correspondant à la sélection de l'utilisateur
if selected_plot == 'Nbr accidents':
    st.pyplot(plot_acc_an_dep(df_car, input_dep))

elif selected_plot == 'Répartition jour / nuit':
    st.pyplot(plot_acc_j_n_dep(df_car, input_dep))

elif selected_plot == 'Agglo / hors agglo':
    st.pyplot(plot_acc_agglo_dep(df_car, input_dep))

elif selected_plot == "Répartition par type d'individu":
    st.pyplot(plot_acc_type_dep(df_merged1, input_dep))

elif selected_plot == 'Répartition de la gravité':
    st.pyplot(plot_acc_gravite_dep(df_merged1, input_dep))

elif selected_plot == 'Répartition par genre':
    st.pyplot(plot_acc_genre_dep(df_merged1, input_dep))

elif selected_plot == 'Localisation par type de véhicule':
    st.pyplot(plot_acc_type_veh_dep(df_merged2, input_dep))

elif selected_plot == 'Répartition par type de route et condition météo':
    st.pyplot(plot_acc_route_meteo_dep(df_merged3, input_dep))
