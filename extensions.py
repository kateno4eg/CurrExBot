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

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest'
                         f'?access_key={ACCESS_KEY}'
                         f'&base={quote_ticker}&symbols={base_ticker}')
        json_response = json.loads(r.content)
        rates = json_response.get('rates')
        base_rate = rates[keys[base]]
        total_base = base_rate * amount

        return round(total_base, 4)

