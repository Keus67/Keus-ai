import streamlit as st
from utils.data import get_cmc_data
from utils.tradingview import get_tradingview_iframe

def afficher():
    st.subheader("📊 Analyse avec CoinMarketCap")
    symbol = st.text_input("Entrez le symbole de la crypto (ex: BTC, ETH)", "BTC").upper()
    cmc_data = get_cmc_data(symbol)

    if cmc_data:
        quote = cmc_data["quote"]["USD"]
        st.write(f"### {cmc_data['name']} ({symbol})")
        st.metric("💰 Prix actuel", f"${quote['price']:,.2f}")
        st.metric("📉 Variation 24h", f"{quote['percent_change_24h']:.2f}%")
        st.metric("🏦 Market Cap", f"${quote['market_cap']:,.0f}")

        st.markdown("### 📈 Graphique TradingView")
        st.components.v1.html(get_tradingview_iframe(symbol), height=400)
    else:
        st.warning("❌ Crypto introuvable ou problème API.")
