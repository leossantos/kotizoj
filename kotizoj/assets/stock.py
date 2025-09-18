from .asset import Asset
import yfinance as yf
from ..utils.log_config import logger



class Stock(Asset):
    def __init__(self, name: str, country: str, quantity: float) -> None:
        logger.info("Initializing stock %s", name)
        self.name = name
        self.country = country
        self.quantity = quantity


    @property
    def price(self):
        logger.info("Getting price of stock %s", self.name)
        ticker = yf.Ticker(f"{self.name}.SA")
        return ticker.info.get("currentPrice")
