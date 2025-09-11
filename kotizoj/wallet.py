from .assets.asset import Asset

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

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    def __str__(self) -> str:
        ret_str = ""
        for asset in self.assets:
            ret_str += f"{asset.name}: R$ {asset.value}\n"
        return ret_str
