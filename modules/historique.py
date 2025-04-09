import streamlit as st

def afficher():
    st.subheader("📈 Historique des prédictions")

    st.markdown("""
    - 02/04/2025 : BTC → Prédiction haussière 🟢 → Résultat : +3.2%
    - 03/04/2025 : ETH → Prédiction stable 🟡 → Résultat : +0.1%
    - 04/04/2025 : XRP → Prédiction baissière 🔴 → Résultat : -1.8%
    """)

    st.info("📦 Historique privé par utilisateur avec statistiques globales anonymes à venir.")
