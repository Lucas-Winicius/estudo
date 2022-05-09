from aiohttp import request
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

dic_requsicao = requisicao.json()

print(dic_requsicao['USDBRL']['bid'])