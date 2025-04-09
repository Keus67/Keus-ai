import requests

CMC_API_KEY = "33c7fecb-a100-450c-b12e-1f33cbec8e67"

def get_cmc_data(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": CMC_API_KEY,
    }
    params = {"symbol": symbol.upper()}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        return r.json()["data"][symbol.upper()]
    return None
