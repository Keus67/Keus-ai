def get_tradingview_iframe(symbole):
    tv_symbol = f"BINANCE:{symbole.upper()}USDT"
    return f'''
        <div class="tradingview-widget-container">
          <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_{symbole}&symbol={tv_symbol}&interval=60&theme=dark&style=1&locale=fr"
          width="100%" height="400" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
        </div>
    '''
