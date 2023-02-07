import requests
import json 

class Pay:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        pass

    def airtime(self, country_to_send, phone_number, value_in_USD, sub_account='', turn_off_notification=False):
        pass

    def chimoney(self, payment_details, sub_account='', turn_off_notification=False):
        uri= 'v0.2/payouts/chimoney'
        # note difference uri and url
        url= f'{self.api_url}/{uri}'
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        payload={
            "chimoneys": payment_details
        }
        if sub_account != '':
            payload['subAccount'] = sub_account
        if turn_off_notification != False:
            payload['turnOffNotification'] = True
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    




        
# obj = Pay()
# obj.airtime(turn_off_notification=False, country_to_send='Ghana', phone_number='254712345678', value_in_USD=3, sub_account='Antony Gakuru')
# obj.chimoney(
#     payment_details=pay_array_of_objects,   
# )