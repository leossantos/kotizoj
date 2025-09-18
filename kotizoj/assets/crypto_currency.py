from .asset import Asset
from ..utils.utils import get_bitcoin, get_brl_dollar_cotation
import logging

logger = logging.getLogger(__name__)


class CryptoCurrency(Asset):
    def __init__(self, name: str, country: str, quantity: float) -> None:
        logger.info("Initializing crypto currency %s", name)
        self.name = name
        self.country = country
        self.quantity = quantity

    @property
    def price(self):
        logger.info("Getting price of crypto currency %s", self.name)
        crypto_price = get_bitcoin()
        dollar_cotation = get_brl_dollar_cotation()
        brl_crypto_price = crypto_price * dollar_cotation
        return brl_crypto_price