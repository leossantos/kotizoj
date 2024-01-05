class Wallet():
    def __init__(self, name, balance, asset_type):
        self.name = name
        self.asset_type = asset_type
        self.balance = balance
        self.assets = []
    
    def add_asset(self, asset):
        self.assets.append(asset)
    
    def show(self):
        print(f"Wallet: {self.name}")
        for asset in self.assets:
            print(f"  {asset.name}")

    def show_balance(self):
        print(f"Balance: {self.balance}")
        for asset in self.assets:
            print(f"  {asset.name}: {asset.price}")
            self.balance += asset.price
        print(f"Total: {self.balance}")