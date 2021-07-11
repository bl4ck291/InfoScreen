import requests


class XCHtoUSD:
    rate = .0

    def __init__(self):
        f = open("CC.apikey", "r")  # .apikey file contains the API Key from CryptoCompare
        key = f.read().strip()
        f.close()
        url = "https://min-api.cryptocompare.com/data/price?fsym=XCH&tsyms=USD&api_key=" + key
        data = requests.get(url)
        data = data.json()
        self.rate = data["USD"]

    def getUSDtoRUB(self):
        return self.rate