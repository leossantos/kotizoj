from kotizoj.wallet import Wallet
from kotizoj.assets.asset import Asset
from kotizoj.assets.stock import Stock
from kotizoj.assets.crypto_currency import CryptoCurrency


def asset_creator(asset_type: str, name: str, country:str, quantity:str) -> Asset: 
    if asset_type == "stock":
        return Stock(name, country, quantity)
    if asset_type == "crypto":
        return CryptoCurrency(name, country, quantity)



if __name__ == "__main__":
    print("Hello, World!")
    first_wallet = Wallet()
    petr3 = asset_creator("stock","PETR3", "Brasil", 10)
    petr4 = asset_creator("stock","PETR4", "Brasil", 10)
    bitcoin = asset_creator("crypto", "Bitcoin", "Brasil", 1)
    first_wallet.add_asset(petr3)
    first_wallet.add_asset(petr4)
    first_wallet.add_asset(bitcoin)
    print(first_wallet)