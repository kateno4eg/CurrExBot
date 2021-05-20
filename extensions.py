import requests
import json
from config import keys, ACCESS_KEY


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

#  r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        r = requests.get(f'https://api.exchangeratesapi.io/v1/convert'
                         f'?access_key = {ACCESS_KEY}'
                         f'& from = {quote_ticker}& to = {base_ticker}'
                         f'& amount = {amount}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
