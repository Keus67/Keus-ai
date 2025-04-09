import streamlit as st

def afficher():
    st.subheader("📰 Actualités crypto")

    important_news = [
        {"titre": "🚨 ETF Bitcoin validé aux USA", "source": "CoinTelegraph"},
        {"titre": "💥 Explosion du volume sur Solana", "source": "Decrypt"}
    ]

    latest_news = [
        {"titre": "📢 Nouveaux listings sur Binance", "source": "Binance"},
        {"titre": "💡 Analyse des mouvements de baleines", "source": "CryptoSlate"},
    ]

    bouton = st.radio("Filtrer par :", ["Les plus importants", "Les plus récents"])

    news_list = important_news if bouton == "Les plus importants" else latest_news

    for item in news_list:
        st.markdown(f"**{item['titre']}**  \n📰 _{item['source']}_")
