import os
import requests


def get_bitcoin():
    url = "https://api.coingecko.com/api/v3//simple/price"
    params = {"vs_currencies": "usd", "ids": "bitcoin"}
    # Pegando a chave da API de uma variável de ambiente
    api_key = os.getenv("COINGECKO_API_KEY")
    headers = {"x-cg-demo-api-key": api_key}

    response = requests.request(
        "GET", url, headers=headers, params=params, timeout=100
    )

    return response.json()["bitcoin"]["usd"]


def get_brl_dollar_cotation():

    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='09-10-2025'&$top=100&$format=json"

    response = requests.request("GET", url,  timeout=100)

    return response.json()["value"][0]["cotacaoVenda"]
