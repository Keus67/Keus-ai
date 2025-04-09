import streamlit as st

# 🔐 Données utilisateurs simulées
users = {
    "keus": "crypto2025",
    "stevan": "bitcoin"
}

def authentifier_utilisateur():
    st.sidebar.title("🔐 Authentification")
    login = st.sidebar.text_input("Nom d'utilisateur")
    password = st.sidebar.text_input("Mot de passe", type="password")
    if login in users and users[login] == password:
        st.sidebar.success(f"Bienvenue {login} !")
        return True
    elif login and password:
        st.sidebar.error("Identifiants invalides.")
    return False
