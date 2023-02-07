import requests
import json 

class Pay:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'
        pass


    def airtime(self, payment_details, sub_account='', turn_off_notification=False):
        uri= f'{self.api_version}/payouts/airtime'
        # note difference uri and url
        url= f'{self.api_url}/{uri}'
        payload = {
            "airtimes": payment_details
            }
        if sub_account != '':
            payload['subAccount'] = sub_account
        if turn_off_notification != False:
            payload['turnOffNotification'] = True
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()


    def chimoney(self, payment_details, sub_account='', turn_off_notification=False):
        ''' Payout Chimoney'''
        # payment_details == array of objects with payout information eg. email, value to send
        uri= f'{self.api_version}/payouts/bank'
        # note difference uri and url
        url= f'{self.api_url}/{uri}'
        payload={
            "chimoneys": payment_details
        }
        if sub_account != '':
            payload['subAccount'] = sub_account
        if turn_off_notification != False:
            payload['turnOffNotification'] = True
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

    
    def giftcard(self, payment_details, sub_account='', turn_off_notification=False):
        uri = f'{self.api_version}/payouts/gift-card'
        url= f'{self.api_url}/{uri}'
        pass

    
    def bank(self, payment_details, sub_account='', turn_off_notification=False):
        uri = f'{self.api_version}/payouts/bank'
        url= f'{self.api_url}/{uri}'
        # example payment_details array
        # payment_details = [
        #     {
        #             "countryToSend": "Kenya",
        #             "account_bank": "044",
        #             "account_number": "0690000032",
        #             "valueInUSD": 10,
        #             "reference": "",
        #             "fullname" : "John Doe"
        #     }
        # ]
        payload = {
            "banks": payment_details
            }
        if sub_account != '':
            payload['subAccount'] = sub_account
        if turn_off_notification != False:
            payload['turnOffNotification'] = True

        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()
