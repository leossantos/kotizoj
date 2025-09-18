from .assets.asset import Asset
import logging

logger = logging.getLogger(__name__)



class Wallet:
    def __init__(self) -> None:
        logger.info("Initializing wallet")
        self.assets = []
        self.allocation = {}
        self.optimal_allocation = {}

    @property
    def total(self):
        logger.info("Calculating total value of wallet")
        return sum(asset.value for asset in self.assets)

    def allocate(self, contribuition: float):
        pass

    def add_asset(self, asset: Asset):
        logger.info("Adding asset %s to wallet", asset.name)
        self.assets.append(asset)

    def __str__(self) -> str:
        ret_str = ""
        for asset in self.assets:
            ret_str += f"{asset.name}: R$ {asset.value}\n"
        ret_str += f"Total: R$ {self.total}\n"
        return ret_str
