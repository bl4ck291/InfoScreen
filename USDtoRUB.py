import requests


class USDtoRUB:

    rates = {}

    def __init__(self):
        f = open("OER.apikey", "r")  # .apikey file contains the APP ID from Open Exchange Rates
        key = f.read().strip()
        f.close()
        url = "https://openexchangerates.org/api/latest.json?app_id=" + key
        data = requests.get(url)
        data = data.json()
        self.rates = data["rates"]

    def getUSDtoRUB(self):
        return self.rates["RUB"]