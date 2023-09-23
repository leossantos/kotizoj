from obj.Wallet import Wallet
from obj.Asset import Asset


# Create wallet
wallet = Wallet("My Wallet", 1000)

# Add assets
wallet.add_asset(Asset("BBAS3", 1, 0.075, True))
wallet.add_asset(Asset("BTLG11", 2, 0.075, True))
wallet.add_asset(Asset("VGIP11", 3, 0.075, True))
wallet.add_asset(Asset("BLAU3", 4, 0.075, True))
wallet.add_asset(Asset("EGIE3", 5, 0.075, True))
wallet.add_asset(Asset("PVBI11", 6, 0.075, True))
wallet.add_asset(Asset("MALL11", 7, 0.075, True))
wallet.add_asset(Asset("HGRU11", 8, 0.075, True))
wallet.add_asset(Asset("AGRO3", 9, 0.075, True))
wallet.add_asset(Asset("IVVB11", 10, 0.075, True))
wallet.add_asset(Asset("B5P211", 11, 0.075, True))
wallet.add_asset(Asset("RBRP11", 12, 0.075, True))
wallet.add_asset(Asset("Tesouro Selic", 13, 0.1, True))

# Show wallet
wallet.show()

# Show balance
wallet.show_balance()

#
