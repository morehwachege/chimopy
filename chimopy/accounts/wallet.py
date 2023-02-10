import requests


class Wallet:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'

    
    def list_wallets(self, sub_account=''):
        uri= f'{self.api_version}/wallets/list'
        url= f'{self.api_url}/{uri}'

        payload={}
        if sub_account != '':
            payload['subAccount'] = sub_account

        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    
    def single_wallet(self, wallet_id, sub_account=''):
        uri= f'{self.api_version}/wallet/lookup'
        url= f'{self.api_url}/{uri}'
        payload = {
            'walletID': wallet_id
        }
        if sub_account != '':
            payload['subAccount'] = sub_account
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()


    def transfer(self, receiver, wallet, amount, sub_account=''):
        uri= f'{self.api_version}/wallet/transfer'
        url= f'{self.api_url}/{uri}'

        payload ={
            'receiver': receiver,
            'wallet': wallet,
            'amount': amount
        }
        if sub_account != '':
            payload['subAccount'] = sub_account
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()