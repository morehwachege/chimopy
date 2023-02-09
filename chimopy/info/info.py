import requests

class Info:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'

    
    def countries(self):
        '''Get a list of all supported airtime countries'''
        
        uri= f'{self.api_version}/info/airtime-countries'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response.json()


    def assets(self, country_code=''):
        uri= f'{self.api_version}/info/assets?countryCode={country_code}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    
    def banks(self, country_code):
        uri= f'{self.api_version}/info/country-banks?countryCode={country_code}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response.json()


    def convert(self, origin_currency, amount_in_origin_currency):
        """ Convert currency to USD"""
        
        uri= f'{self.api_version}/info/local-amount-in-usd?originCurrency={origin_currency}&amountInOriginCurrency={amount_in_origin_currency}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response.json()