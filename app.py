import streamlit as st
from modules import analyse, prediction, commerce, compareteur, actualites, calendrier, securite, historique, tendances
from modules.auth import authentifier_utilisateur

st.set_page_config(page_title="Keus Assist – IA Crypto Pro", layout="wide")

# Authentification
if not authentifier_utilisateur():
    st.stop()

# Menu principal
menu = st.sidebar.selectbox("📂 Menu", [
    "Accueil", "Analyse Crypto", "Prédictions", "Commerce", "Comparateur",
    "Actualités", "Calendrier", "Sécurité", "Historique", "Tendances"
])

# Routing vers modules
if menu == "Accueil":
    st.title("👋 Bienvenue sur Keus Assist – IA Crypto Pro")
    st.success("Sélectionne un module dans le menu de gauche.")
elif menu == "Analyse Crypto":
    analyse.afficher()
elif menu == "Prédictions":
    prediction.afficher()
elif menu == "Commerce":
    commerce.afficher()
elif menu == "Comparateur":
    compareteur.afficher()
elif menu == "Actualités":
    actualites.afficher()
elif menu == "Calendrier":
    calendrier.afficher()
elif menu == "Sécurité":
    securite.afficher()
elif menu == "Historique":
    historique.afficher()
elif menu == "Tendances":
    tendances.afficher()
