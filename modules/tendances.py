import streamlit as st

def afficher():
    st.subheader("📊 Crypto en tendance")

    intervalle = st.selectbox("Intervalle de temps", ["1h", "24h"])
    st.info(f"📡 Données actuelles basées sur l’intervalle sélectionné : {intervalle}")

    st.markdown("""
    ### 🚀 Top 10 des cryptos en hausse
    1. TAO +25%
    2. SOL +18%
    3. INJ +16%
    ...
    
    ### 📉 Top 10 des cryptos en baisse
    1. SHIB -12%
    2. DOGE -10%
    3. PEPE -8%
    ...
    """)

    if st.checkbox("🔄 Activer l'affichage en direct (optionnel)"):
        st.success("🕒 Actualisation automatique activée.")
