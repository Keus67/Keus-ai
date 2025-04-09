import streamlit as st

def afficher():
    st.subheader("🔍 Comparateur de prix")

    st.markdown("""
    | Plateforme | Prix BTC (exemple) |
    |------------|--------------------|
    | Binance    | $29,800            |
    | MEXC       | $29,850            |
    | KuCoin     | $29,820            |
    | Crypto.com | $29,790            |
    """)

    st.info("🔁 Données à jour toutes les 5 minutes (source : CoinMarketCap/TradingView)")
