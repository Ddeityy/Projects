r = requests.get("https://api.exchangerate.host/latest")
rates = r.json.loads(r.content)["rates"]
print(rates)