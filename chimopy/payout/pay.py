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
        pass

    def airtime(self, country_to_send, phone_number, value_in_USD, sub_account='', turn_off_notification=False):
        pass

    def chimoney(self, payment_details, sub_account='', turn_off_notification=False):
        uri= 'v0.2/payouts/chimoney'
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
        uri = 'v0.2/payouts/gift-card'
        url= f'{self.api_url}/{uri}'
        pass



        
# obj = Pay()
# obj.airtime(turn_off_notification=False, country_to_send='Ghana', phone_number='254712345678', value_in_USD=3, sub_account='Antony Gakuru')
# obj.chimoney(
#     payment_details=pay_array_of_objects,   
# )