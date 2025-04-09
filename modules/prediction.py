import streamlit as st
from utils.ai import prediction_ia

def afficher():
    st.subheader("🔮 Prédiction IA")

    crypto = st.text_input("Crypto ciblée (ex: BTC, ETH)", "BTC").upper()
    if not crypto:
        st.warning("Veuillez entrer un symbole.")
        return

    if st.button("Lancer la prédiction IA"):
        resultat, confiance, tendance = prediction_ia(crypto)
        st.success(f"📈 Résultat : {resultat}")
        st.metric("🔎 Confiance IA", f"{confiance}%")
        st.info(f"Tendance détectée : {tendance}")

    if st.checkbox("📊 Voir les 3 scénarios possibles (positif / neutre / négatif)"):
        st.markdown("""
        - ✅ **Scénario positif** : hausse jusqu’à +12% estimée
        - ⚖️ **Scénario neutre** : oscillation stable dans une zone de range
        - ❌ **Scénario négatif** : chute possible vers -8%
        """)

    if st.toggle("📅 Prédire à une date ultérieure"):
        date = st.date_input("Choisir une date")
        st.success(f"Prédiction pour {crypto} à la date : {date} → (IA à compléter)")
