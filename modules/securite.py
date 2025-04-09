import streamlit as st

def afficher():
    st.subheader("🔐 Conseils de sécurité")

    st.markdown("""
    - Utilise un **cold wallet** pour stocker tes actifs importants.
    - Active le **2FA** (authentification à deux facteurs).
    - Ne partage **jamais** ta seed phrase.
    - Vérifie les projets **audités** (via CertiK, Hacken, etc).
    - Reste informé via des sources fiables.
    """)
