import yfinance as yf

class Asset():
    def __init__(self, name, priority, balance, buy):
        self.name = name
        self.priority = priority
        self.balance = balance
        self.buy = buy
        self.price = self.get_price()
    
    def get_price(self):
        if self.name == "Tesouro Selic":
            return 13207.00
        asset = yf.Ticker(f"{self.name}.SA")
        price = asset.fast_info['lastPrice']
        return price