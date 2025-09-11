from .asset import Asset
from ..utils.utils import get_bitcoin, get_brl_dollar_cotation


class CryptoCurrency(Asset):
    def __init__(self, name: str, country: str, quantity: float) -> None:
        self.name = name
        self.country = country
        self.quantity = quantity

    @property
    def value(self):
        return self.quantity * self.price

    @property
    def price(self):
        crypto_price = get_bitcoin()
        dollar_cotation = get_brl_dollar_cotation()
        brl_crypto_price = crypto_price * dollar_cotation
        return brl_crypto_price