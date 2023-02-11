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
        return response


    def assets(self, country_code=''):
        ''' Get a list of chimoney assets '''

        uri= f'{self.api_version}/info/assets?countryCode={country_code}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response

    
    def banks(self, country_code):
        ''' Get infomation about supported banks'''

        uri= f'{self.api_version}/info/country-banks?countryCode={country_code}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response


    def convert_local(self, origin_currency, amount_in_origin_currency):
        """ Convert local currency to USD"""

        uri= f'{self.api_version}/info/local-amount-in-usd?originCurrency={origin_currency}&amountInOriginCurrency={amount_in_origin_currency}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response

    def convert_usd(self, destination_currency, amount_in_usd):
        """ Convert USD currency to local currency"""

        uri= f'{self.api_version}/info/usd-amount-in-local?destinationCurrency={destination_currency}&amountInUSD={amount_in_usd}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)
        return response
    
    def momo(self):
        ''' Get supported mobile money code'''

        uri= f'{self.api_version}/info/mobile-money-codes'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers)

    def verify(self, accounts_information):
        ''' Verify bank account '''
        uri= f'{self.api_version}/info/verify-bank-account-number'
        url= f'{self.api_url}/{uri}'
        payload = {
            'verifyAccountNumbers': accounts_information
        }
        response = requests.post(url, headers=self.headers, json=payload)

        return response