from ..utils.log_config import logger

logger.name = __name__

class Asset():
    def __init__(self, name: str, country: str, quantity: float) -> None:
        logger.info("Initializing asset %s", name)
        self.name = name
        self.country = country
        self.quantity = quantity

    @property
    def value(self):
        logger.info("Calculating value of asset %s", self.name)
        return round(self.quantity * self.price, 2)

    @property
    def price(self):
        pass