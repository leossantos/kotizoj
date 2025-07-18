```mermaid
---
title: Kotizoj (Modelo Refatorado)
---
classDiagram
    class WalletCreator {
        create_wallet() Wallet
    }
    class Wallet {
        List<Asset> assets
        Dict<String, float> allocation
        get_total_value() float
    }
    Wallet o-- Asset

    class AssetCreator {
        <<abstract>>
        factory_method(params) Asset
    }
    AssetCreator <|-- BondCreator
    class BondCreator {
        factory_method(params) Asset
    }

    class Asset {
        <<abstract>>
        string name
        string country
        float quantity
        get_value() float
        get_price() float
    }

    Asset <|-- Bond
    class Bond {
        <<abstract>>
        date expiration_date
    }

    Bond <|-- TreasuryBond
    class TreasuryBond {
        <<abstract>>
        string issuer "Tesouro Nacional"
    }

    TreasuryBond <|-- TreasurySelic
    TreasuryBond <|-- TreasuryIPCA
    TreasuryBond <|-- TreasuryPrefixed
    class TreasurySelic {
        string index_type "SELIC"
    }
    class TreasuryIPCA {
        string index_type "IPCA"
        float fixed_rate
    }
    class TreasuryPrefixed {
        float fixed_rate
    }

    Asset <|-- Stock
    class Stock {
        string stock_exchange
    }

    Asset <|-- ETF
    class ETF {
        string stock_exchange
        string etf_type
        string tracking_index
    }

    Asset <|-- CryptoCurrency
    class CryptoCurrency {
    }
```

