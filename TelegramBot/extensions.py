import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(base: str, to: str, amount: str):        
        
        if base == to:
            raise ConversionException(f"Невозможно перевести одинаковые валюты {to}.")
        
        try:
            base_ticket = keys[base]
        except KeyError:
            raise ConversionException(f"Невозможно обработать валюту {base}.")
        
        try:
            base_ticket = keys[to]
        except KeyError:
            raise ConversionException(f"Невозможно обработать валюту {to}.")
        
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Не удалось обработать количество {amount}.")

        base_ticket, to_ticket = keys[base], keys[to]
        
        r = requests.get(f"https://api.exchangerate.host/convert?from={base_ticket}&to={to_ticket}&amount={amount}")
        result = json.loads(r.content)["result"]
        
        return result