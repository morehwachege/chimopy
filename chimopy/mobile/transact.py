import requests 


class Transaction:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'

    def pay(self, payment_details, sub_account=''):
        ' Pay using mobile money'
        uri = f'{self.api_version}/collections/mobile-money/collect'
        url = f'{self.api_url}/{uri}'
        payload = payment_details
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    def transactions(self, sub_account='', turn_off_notification=False):
        ''' List all mobile money transactions '''

        uri = f'{self.api_version}/collections/mobile-money/all'
        url = f'{self.api_url}/{uri}'
        payload = {}
        if sub_account != '':
            payload['subAccount'] = sub_account

        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
