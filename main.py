import streamlit as st
from PIL import Image

from data_viz_cleaning.caracteristiques import df_clean_car
from data_analysis_france import plot_acc_an, plot_acc_j_n, plot_acc_agglo, plot_acc_gravite, plot_acc_genre
from data_analysis_dep import plot_acc_an_dep, plot_acc_j_n_dep, plot_acc_agglo_dep, plot_acc_gravite_dep, plot_acc_genre_dep
from data_viz_cleaning.merged import merged_car_lie, merged_car_usag, merged_car_veh

# Définir la couleur de fond de la page
st.set_page_config(page_title="Prevent-Corp")



@st.cache_data
def load_df_car():
    return df_clean_car()

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

link_format = lambda name: f'<a class="{"active" if choice==name else ""}" href="?choice={name}" target="_self">{name}</a>'
menu_links = "".join([link_format(name) for name in menu])

st.markdown(f'<div class="navbar">{menu_links}</div>', unsafe_allow_html=True)

# Afficher la page sélectionnée
if choice == "Accueil":
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


elif choice == "Visualisation":
    st.title("Statistiques des 10 dernières années en France")
    # Inclure le graphique
    st.pyplot(plot_acc_an(df_car))
    st.markdown("<br>", unsafe_allow_html=True)

    st.pyplot(plot_acc_j_n(df_car))
    st.markdown("<br>", unsafe_allow_html=True)

    st.pyplot(plot_acc_agglo(df_car))
    st.markdown("<br>", unsafe_allow_html=True)

    st.pyplot(plot_acc_gravite(df_merged1))
    st.markdown("<br>", unsafe_allow_html=True)

    st.pyplot(plot_acc_genre(df_merged1))
    st.markdown("<br>", unsafe_allow_html=True)


elif choice == "Prédiction":
    st.title("Prédiction d'un département !")
    st.write("Pour ce projet, nous ne disposions pas de suffissament de données pour proposer des prédictions sur les départements hors france métropolitaine")

    input_dep = st.number_input("Entrez le numéro du département (1 à 95) :", value=75)

    st.write(f"<h3 style='text-align: center; font-size: 25px;'>Prédiction du nombre d'accident pour le département | {input_dep} |</h3>", unsafe_allow_html=True)
    st.write("En attente...")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.write(f"<h3 style='text-align: center; font-size: 25px;'>Statistiques des 10 dernières années pour le département | {input_dep} |</h3>", unsafe_allow_html=True)

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
    plot_names = ['Nbr accidents', 'Répartition jour / nuit', 'Agglo / hors agglo', 'Répartition de la gravité', 'Répartition par genre']

    # Menu déroulant pour sélectionner le plot
    selected_plot = st.selectbox('Sélectionnez un graph à afficher', plot_names)

    # Affichage du plot correspondant à la sélection de l'utilisateur
    if selected_plot == 'Nbr accidents':
        st.pyplot(plot_acc_an_dep(df_car, input_dep))
    elif selected_plot == 'Répartition jour / nuit':
        st.pyplot(plot_acc_j_n_dep(df_car, input_dep))
    elif selected_plot == 'Agglo / hors agglo':
        st.pyplot(plot_acc_agglo_dep(df_car, input_dep))
    elif selected_plot == 'Répartition de la gravité':
        st.pyplot(plot_acc_gravite_dep(df_merged1, input_dep))
    elif selected_plot == 'Répartition par genre':
        st.pyplot(plot_acc_genre_dep(df_merged1, input_dep))


    # Définition des plots

    # plot1 = plot_acc_an_dep(df_car, input_dep)
    # plot2 = plot_acc_j_n_dep(df_car, input_dep)
    # plot3 = plot_acc_agglo_dep(df_car, input_dep)
    # plot4 = plot_acc_gravite_dep(df_merged1, input_dep)

    # # Affichage des plots

    # col1, col2 = st.columns(2)
    # col1.pyplot(plot_acc_an_dep(df_car, input_dep))
    # col2.pyplot(plot_acc_j_n_dep(df_car, input_dep))

    # col3, col4 = st.columns(2)
    # col3.pyplot(plot3)
    # col4.pyplot(plot4)


elif choice == "Suggestion":
    st.title("Suggestion de prevent corp")
    # Ajouter le contenu de la page 3 ici


# Page L'équipe
if choice == "L'équipe":
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
