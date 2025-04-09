def prediction_ia(symbole):
    symbole = symbole.upper()
    if symbole == "BTC":
        return "Hausse possible", 92, "🚀 Forte tendance haussière"
    elif symbole == "ETH":
        return "Stabilité attendue", 85, "📊 Zone de consolidation"
    else:
        return "Analyse limitée", 70, "🔍 Analyse standard"

def analyse_ia_crypto(symbole, niveau_risque):
    base_price = 100
    if niveau_risque == "Faible":
        return base_price * 1.03, base_price * 0.98, "📈 Prédiction IA fiable"
    elif niveau_risque == "Moyen":
        return base_price * 1.07, base_price * 0.94, "📉 Prédiction modérée"
    else:
        return base_price * 1.15, base_price * 0.85, "⚠️ Prédiction risquée"
