import requests 


class Transaction:
    def __init__(
        self, 
        base_url= 'https://chimoney-backend-api-sandbox.onrender.com/v0.2/collections/mobile-money/all',
        api_key = None,
        params = {} ):
        self.base_url = base_url
        self.params = params
        self.headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'X-API-KEY': api_key
        }
        pass

    def transact(self):
        print(self.base_url)
        res = requests.post(f'{self.base_url}/v0.2/collections/mobile-money/collect', headers=self.headers,
        params=self.params
        )
        return res.json()

    def list_transactions(self):
        pass
url = 'https://chimoney-backend-api-sandbox.onrender.com/v0.2/collections/mobile-money/collect'
key = '8db691db5747c3b0f1bbbfa81d61bef2c0dc8dae7be2557fbb8db783451cddeb'
parameters = {
    'amount': 2,
    'currency': 'usd',
    'phone_number': '254740480364',
    'fullname': 'Antony Gakuru',
    'country': 'Kenya',
    'tx-ref': '2123132342',
    'subAccount': '23423efdfvd23'
}
send = Transaction(base_url=url ,api_key=key, params=parameters)