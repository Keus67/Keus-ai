import streamlit as st

def afficher():
    st.subheader("📆 Calendrier des événements crypto")

    st.markdown("""
    - 🪙 **Listing** : Nouvelle crypto ajoutée sur une plateforme.
    - 🔥 **Token Burn** : Destruction de tokens pour réduire l'offre.
    - 🍴 **Hard Fork** : Mise à jour majeure du protocole.
    - ⛓️ **Unlock** : Libération de tokens bloqués.
    - 📈 **Bullrun Estimé** : Analyse prédictive d’un marché haussier.
    """)

    st.info("🔎 Utilise la barre de recherche pour filtrer un événement (fonctionnalité à venir).")
