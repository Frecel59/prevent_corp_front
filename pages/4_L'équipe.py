import streamlit as st
from PIL import Image
import pandas as pd

from data_viz_cleaning.caracteristiques import df_clean_car
from data_analysis_france import plot_acc_an, plot_acc_j_n, plot_acc_agglo, plot_acc_gravite, plot_acc_genre
from data_analysis_dep import plot_acc_an_dep, plot_acc_j_n_dep, plot_acc_agglo_dep, plot_acc_gravite_dep, plot_acc_genre_dep
from data_viz_cleaning.merged import merged_car_lie, merged_car_usag, merged_car_veh

# Définir la couleur de fond de la page
st.set_page_config(page_title="Prevent-Corp", initial_sidebar_state="collapsed")





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
link_format = lambda i, name: f'<a class="{"active" if choice==name else ""}" href="{name}" target="_self">{name}</a>'
menu_links = "".join([link_format(i, name) for i, name in enumerate(menu)])

st.markdown(f'<div class="navbar">{menu_links}</div>', unsafe_allow_html=True)

# Afficher la page sélectionnée


# Page L'équipe

st.title("Notre équipe")

# Liste des membres de l'équipe avec leurs coordonnées et liens LinkedIn
team_members = [
    {
        "name": "Cédric Lecerf",
        "dep" : "Nord",
        "photo": "https://media.licdn.com/dms/image/D4E03AQE6kOrDApGAVA/profile-displayphoto-shrink_200_200/0/1679247325960?e=1685577600&v=beta&t=cVJVZepnGvN27w_hvgCLR96PggBq7vuB5xqkErYUL8A",
        "linkedin": "https://www.linkedin.com/in/cedriclecerf59/",
    },
    {
        "name": "Victor Siesse",
        "dep" : "Val de Marne",
        "photo": "https://media.licdn.com/dms/image/C4E03AQGHA__1QlaU1A/profile-displayphoto-shrink_800_800/0/1643055015651?e=1685577600&v=beta&t=YUQmVZ8Chm1yaIPqztmyDrTTB1DpjbIOZn9vIiMOPj8",
        "linkedin": "https://www.linkedin.com/in/victor-siesse-a0a2aa22a/",
    },
    {
        "name": "Arnaud Pelet",
        "dep" : "Gard",
        "photo": "https://media.licdn.com/dms/image/C4E03AQHzH0q04H1G6Q/profile-displayphoto-shrink_800_800/0/1643365668984?e=1685577600&v=beta&t=qpTa5LW4zc5QbjlaW0qxXYhkfcWfrfn3vmxNiCke0MY",
        "linkedin": "https://www.linkedin.com/in/arnaud-pelet/",
    },
    {
        "name": "Tituan De Radigues",
        "dep" : "Wallonie",
        "photo": "https://media.licdn.com/dms/image/D4E03AQEXXcE_r1DtTw/profile-displayphoto-shrink_800_800/0/1680267112765?e=1685577600&v=beta&t=T7-Bdd36_GFBlgA-ejaXN2p_3NBdheqEEWm0rud9lFA",
        "linkedin": "https://www.linkedin.com/in/titouan-de-radigues-32b432240/",
    },
]

# Charger l'icône LinkedIn
linkedin_icon = "https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg"

# Affichage des membres de l'équipe
cols = st.columns(4)
for i, member in enumerate(team_members):
    cols[i].image(member["photo"], width=150)
    cols[i].markdown(
        f"""
        <p style='text-align: center;'>
            <span>{member['name']}</span><br />
            <span>{member['dep']}</span><br />
            <a href='{member['linkedin']}'><img src='{linkedin_icon}' alt='LinkedIn' width='25' /></a>
        </p>
        """,
        unsafe_allow_html=True,
    )



# Remerciements aux enseignants
st.subheader("Remerciements à nos enseignants")
st.write("Un grand merci à nos deux Teachers, Marguerite et Aloys, pour leur soutien et leur guidance tout au long du projet.")

# Remerciements au gouvernement
st.subheader("Remerciements au gouvernement")
st.write("Nous tenons également à remercier le gouvernement pour nous avoir permis d'utiliser les données des accidents de la route en France. Leur collaboration a été essentielle pour le développement de notre projet.")
