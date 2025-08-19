class Asset():
    def __init__(self, name: str, country: str, quantity: float) -> None:
        self.name = name
        self.country = country
        self.quantity = quantity

    @property
    def value(self):
        pass

    @property
    def price(self):
        pass