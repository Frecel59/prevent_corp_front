import streamlit as st
from PIL import Image
import pandas as pd

from data_viz_cleaning.caracteristiques import df_clean_car
from data_analysis_france import plot_acc_an, plot_acc_j_n, plot_acc_agglo, \
    plot_acc_gravite, plot_acc_genre, plot_acc_type, plot_acc_type_veh, \
    plot_acc_route_meteo
from data_viz_cleaning.merged import merged_car_lie, merged_car_usag, \
    merged_car_veh

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

st.title("Statistiques des 10 dernières années en France")
# Inclure le graphique
# st.pyplot(plot_acc_an(df_car))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_j_n(df_car))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_agglo(df_car))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_gravite(df_merged1))
# st.markdown("<br>", unsafe_allow_html=True)

# st.pyplot(plot_acc_genre(df_merged1))
# st.markdown("<br>", unsafe_allow_html=True)


plot_names = ['Nbr accidents', 'Répartition jour / nuit', 'Agglo / hors agglo',\
    "Répartition par type d'individu", 'Répartition de la gravité', \
    'Répartition par genre', 'Localisation par type de véhicule',\
    'Répartition par type de route et condition météo']

# Menu déroulant pour sélectionner le plot
selected_plot = st.selectbox('Sélectionnez un graph à afficher', plot_names)
# st.markdown("<br>", unsafe_allow_html=True)

# Affichage du plot correspondant à la sélection de l'utilisateur
if selected_plot == 'Nbr accidents':
    st.write("La répartition du nombre d'accidents en France sur les 10 \
    dernières années montre une diminution progressive depuis 2011, avec une \
    légère remontée en 2017 et 2018, avant de baisser à nouveau en 2019 et 2020.\
    Cette année-là a connu une baisse significative du nombre d'accidents de la \
    route en raison de la pandémie de Covid-19 et des mesures de confinement \
    mises en place, mettant en lumière l'impact des déplacements routiers sur \
    le nombre d'accidents.")
    st.pyplot(plot_acc_an(df_car))

elif selected_plot == 'Répartition jour / nuit':
    st.write("Répartition des accidents selon le moment de la journée, avec une \
    différence significative entre les accidents survenant en journée (75 %) et\
    ceux survenant la nuit (25 %)")
    st.pyplot(plot_acc_j_n(df_car))

elif selected_plot == 'Agglo / hors agglo':
    st.write("Cette représentation met en évidence que les accidents survenus \
        en France ont majoritairement lieu en zone urbaine, tandis que les \
        conditions météorologiques normales sont les plus fréquentes. Ces \
        informations peuvent aider à cibler les efforts de prévention des \
        accidents de la route.")
    st.pyplot(plot_acc_agglo(df_car))

elif selected_plot == "Répartition par type d'individu":
    st.write("La répartition des accidents en France par type d'individu montre \
    que les conducteurs sont les plus touchés, avec plus de 74 % des accidents \
    recensés. Les passagers représentent environ 17 % des accidents, tandis \
    que les piétons sont impliqués dans environ 8 % des accidents. Cette \
    répartition souligne l'importance de la sensibilisation à la \
    sécurité routière pour tous les usagers de la route.")
    st.pyplot(plot_acc_type(df_merged1))

elif selected_plot == 'Répartition de la gravité':
    st.write("En France, la majorité des accidents ont entraîné des blessures \
        avec hospitalisation (55,64 %), soulignant l'importance de la sécurité \
        routière et de la prévention des accidents pour réduire le nombre \
        de blessés sur les routes.")
    st.pyplot(plot_acc_gravite(df_merged1))

elif selected_plot == 'Répartition par genre':
    st.write("La répartition des accidents en France selon le genre révèle que \
        les hommes sont impliqués dans près de 70 % des accidents, contre 32 % \
        pour les femmes.")
    st.pyplot(plot_acc_genre(df_merged1))

elif selected_plot == 'Localisation par type de véhicule':
    st.write("Répartition des accidents en France en fonction du type de \
        véhicule impliqué. On constate que les véhicules légers sont les plus \
        fréquemment impliqués dans des accidents (67 %), suivis des deux-roues \
        (28 %) et des poids lourds et transports en commun (4 %).")
    st.pyplot(plot_acc_type_veh(df_merged2))

elif selected_plot == 'Répartition par type de route et condition météo':
    st.write("On peut observer que les accidents ont lieu majoritairement sur \
        les voies et les routes, avec une proportion plus importante sur les \
        voies. Par ailleurs, on constate que la grande majorité des accidents \
        surviennent par temps sec, tandis que les conditions météorologiques\
        humides ou gelées sont impliquées dans un peu moins d'un quart \
        des accidents.")
    st.pyplot(plot_acc_route_meteo(df_merged3))
