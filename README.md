# kotizoj

## Sobre o Projeto

O **kotizoj** é uma biblioteca Python para gerenciamento de carteira de investimentos que permite acompanhar e calcular o valor de diferentes tipos de ativos financeiros. O projeto oferece uma estrutura modular para trabalhar com ações, ETFs, criptomoedas e títulos do tesouro.

## Funcionalidades

- **Gestão de Carteira**: Classe `Wallet` para organizar e gerenciar múltiplos ativos
- **Suporte a Múltiplos Ativos**:
  - **Ações**: Integração com Yahoo Finance para cotações em tempo real
  - **ETFs**: Cálculo de valores baseado em cotações do mercado brasileiro
  - **Criptomoedas**: Preços em tempo real via CoinGecko API
  - **Títulos do Tesouro**: Suporte para títulos de renda fixa (em desenvolvimento)
- **Cálculos Automáticos**: Valor total da carteira baseado em preços atuais
- **Integração com APIs**: Yahoo Finance e CoinGecko para dados em tempo real
- **Conversão de Moedas**: Cálculo automático de cotações USD/BRL

## Tecnologias Utilizadas

- Python 3.12+
- yfinance (integração com Yahoo Finance)
- requests (chamadas para APIs externas)
- CoinGecko API (preços de criptomoedas)
- Banco Central do Brasil API (cotações de moedas)

## Estrutura do Projeto

```
kotizoj/
├── assets/          # Classes de diferentes tipos de ativos
├── utils/           # Utilitários para APIs externas
└── wallet.py        # Classe principal para gestão da carteira
```
