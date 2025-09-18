from .assets.asset import Asset
from .utils.log_config import logger


logger.name = __name__

class Wallet:
    def __init__(self) -> None:
        logger.info("Initializing wallet")
        self.assets = []
        self.allocation = {}
        self.optimal_allocation = {}

    @property
    def total(self):
        pass

    def allocate(self, contribuition: float):
        pass

    def add_asset(self, asset: Asset):
        logger.info("Adding asset %s to wallet", asset.name)
        self.assets.append(asset)

    def __str__(self) -> str:
        ret_str = ""
        for asset in self.assets:
            ret_str += f"{asset.name}: R$ {asset.value}\n"
        return ret_str
