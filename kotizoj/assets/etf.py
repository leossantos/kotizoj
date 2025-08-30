from .asset import Asset
import yfinance as yf


class ETF(Asset):
    def __init__(self, name: str, country: str, quantity: float) -> None:
        self.name = name
        self.country = country
        self.quantity = quantity


    @property
    def value(self):
        return self.quantity * self.price


    @property
    def price(self):
        ticker = yf.Ticker(f"{self.name}.SA")
        return ticker.info.get("currentPrice")
