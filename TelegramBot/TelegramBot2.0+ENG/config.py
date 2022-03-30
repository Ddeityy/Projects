import requests
import json

TOKEN = "5178989633:AAEbMsFV8sx8lmjcSk7hWa0ae6xhcpnJSeg"

r = requests.get("https://api.exchangerate.host/latest")
rates_dict = json.loads(r.content)["rates"]
rates_keys = list(rates_dict.keys())
rates_keyz = {i : i for i in rates_keys}

