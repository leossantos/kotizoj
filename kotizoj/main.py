from .wallet import Wallet
from .assets.asset import Asset
from .assets.stock import Stock


def asset_creator(asset_type: str, name: str, country:str, quantity:str) -> Asset: 
    if asset_type == "stock":
        return Stock(name, country, quantity)



if __name__ == "__main__":
    print("Hello, World!")
    first_wallet = Wallet()
    petr3 = asset_creator("stock","PETR3", "Brasil", 10)
    petr4 = asset_creator("stock","PETR4", "Brasil", 10)
    first_wallet.add_asset(petr3)
    first_wallet.add_asset(petr4)
    print(first_wallet)
