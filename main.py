from kotizoj.wallet import Wallet
from kotizoj.assets import Asset, Stock, CryptoCurrency, ETF
from kotizoj.utils.log_config import logger


def asset_creator(asset_type: str, name: str, country:str, quantity:str) -> Asset: 
    if asset_type == "stock":
        return Stock(name, country, quantity)
    if asset_type == "crypto":
        return CryptoCurrency(name, country, quantity)
    if asset_type == "etf":
        return ETF(name, country, quantity)
    logger.error("Invalid asset type: %s", asset_type)
    raise ValueError(f"Invalid asset type: {asset_type}")



if __name__ == "__main__":
    logger.info("Starting Kotizoj")
    first_wallet = Wallet()
    agro3 = asset_creator("stock","AGRO3", "Brasil", 8)
    b5p211 = asset_creator("etf","B5P211", "Brasil", 10)
    bbas3 = asset_creator("stock","BBAS3", "Brasil", 8)
    blau3 = asset_creator("stock","BLAU3", "Brasil", 20)
    bovv11 = asset_creator("etf","BOVV11", "Brasil", 7)
    egie3 = asset_creator("stock","EGIE3", "Brasil", 5)
    ivvb11 = asset_creator("etf","IVVB11", "Brasil", 5)
    wrld11 = asset_creator("etf","WRLD11", "Brasil", 14)
    bitcoin = asset_creator("crypto", "Bitcoin", "Brasil", 0.00090177)
    first_wallet.add_asset(agro3)
    first_wallet.add_asset(b5p211)
    first_wallet.add_asset(bbas3)
    first_wallet.add_asset(blau3)
    first_wallet.add_asset(bovv11)
    first_wallet.add_asset(egie3)
    first_wallet.add_asset(ivvb11)
    first_wallet.add_asset(wrld11)
    first_wallet.add_asset(bitcoin)
    print(first_wallet)