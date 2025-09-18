from .asset import Asset
import yfinance as yf
import logging

logger = logging.getLogger(__name__)

class ETF(Asset):
    def __init__(self, name: str, country: str, quantity: float) -> None:
        logger.info("Initializing etf %s", name)
        self.name = name
        self.country = country
        self.quantity = quantity



    @property
    def price(self):
        logger.info("Getting price of etf %s", self.name)
        ticker = yf.Ticker(f"{self.name}.SA")
        return ticker.info.get("currentPrice")
