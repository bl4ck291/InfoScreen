import requests


# Open Exchange Rates
class OERUSDtoRUB:
    f = open("key.apikey", "r")  # .apikey file contains the APP ID from Open Exchange Rates
    key = f.read().strip()
    f.close()
    url = "https://openexchangerates.org/api/latest.json?app_id=" + key
    rates = {}

    def __init__(self):
        data = requests.get(self.url)
        data = data.json()
        self.rates = data["rates"]

    def getUSDtoRUB(self):
        return self.rates["RUB"]


converter = OERUSDtoRUB()

print(round(converter.getUSDtoRUB(), 2))
