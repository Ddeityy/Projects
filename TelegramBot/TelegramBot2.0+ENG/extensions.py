from babel import numbers
import requests
import json
from config import rates_keyz

class ConversionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(base: str, to: str, amount: str):        
        
        
        
        if base == to:
            raise ConversionException("Can't convert identical currencies.")
        
        try:
            base_ticket = rates_keyz[base]
        except KeyError:
            raise ConversionException(f"Currency '{base}' is not avalible.")
        
        try:
            base_ticket = rates_keyz[to]
        except KeyError:
            raise ConversionException(f"Currency '{to}' is not avalible.")
        
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Can't process '{amount}'.")

        base_ticket, to_ticket = rates_keyz[base], rates_keyz[to]
        
        
        r = requests.get(f"https://api.exchangerate.host/convert?from={base_ticket}&to={to_ticket}&amount={amount}")
        res = json.loads(r.content)["result"]
        result = numbers.format_currency(res, to, u'#,##0.00 ¤¤¤', locale='en')
        
        return result