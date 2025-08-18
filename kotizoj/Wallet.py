from .assets.Asset import Asset
class Wallet:
    def __init__(self) -> None:
        self.assets = []
        self.allocation = {}
        self.optimal_allocation = {}

    @property
    def total(self):
        pass

    def allocate(self, contribuition: float):
        pass

    def add_asset(self, assets: Asset):
        pass
