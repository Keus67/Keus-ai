import streamlit as st
from utils.ai import analyse_ia_crypto

def afficher():
    st.subheader("💹 Stratégie de commerce IA")

    symbole = st.text_input("Crypto ciblée (ex: BTC)", "BTC").upper()
    risque = st.radio("Niveau de risque", ["Faible", "Moyen", "Élevé"])

    if symbole:
        tp, sl, prediction = analyse_ia_crypto(symbole, risque)

        st.metric("🎯 Take Profit", f"{tp}")
        st.metric("🛡️ Stop Loss", f"{sl}")
        st.info(f"🧠 Prédiction IA : {prediction}")

        if st.toggle("📊 Voir analyse complète"):
            st.markdown("👉 [Analyse technique à venir ici]")

        st.markdown("⚠️ Ajuste les valeurs selon ta stratégie.")
