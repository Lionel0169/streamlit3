import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format 

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "nom_cookie",
    "cle_signature",
    30
)

authenticator.login()
def accueil():
    if st.session_state["authentication_status"]:
        accueil()
        st.image("gettyimages-1330989185-612x612.jpg")
    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')
    

with st.sidebar :   
    authenticator.logout("Déconnexion")
    st.write("Bienvenue!")
    selection = option_menu(
                menu_title=None,
                options = ["Accueil", "Photos"])

    st.title("Bienvenue sur ma page")
    
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
    st.image("gettyimages-1330989185-612x612.jpg")
elif selection == "Photos":
    st.write("Bienvenue dans  mon album photo")
    col1, col2, col3 = st.columns(3)
    with col1:
                st.image("belgian-malinois-running-autumn-field-600nw-2716105475.webp")
    with col2:
                st.image("blog-breed-malinois_1.max-500x500.format-jpeg.jpg")
    with col3:
                st.image("632c61510643ed413287f04c_Races-Berger-Belge-Malinois_lvllzc.jpg")

    
        
    
