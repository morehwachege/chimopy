import requests
import json 

class Pay:
    def __init__(self):
        pass

    def airtime(self, country_to_send, phone_number, value_in_USD, sub_account='', turn_off_notification=False):
        pass

    def chimoney(self, payment_details, sub_account='', turn_off_notification=False):
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": "8db691db5747c3b0f1bbbfa81d61bef2c0dc8dae7be2557fbb8db783451cddeb"
        }
        payload={
            "chimoneys": payment_details
        }
        if sub_account != '':
            payload['subAccount'] = sub_account
        if turn_off_notification != False:
            payload['turnOffNotification'] = True
        response = requests.post(url, headers=headers, json=payload)
        print(response.json())
pay_array_of_objects = [
        {
            "email": "mail@mailer10.ca",
            "valueInUSD": 1
        },
        {
            "twitter": "@TWITTERNAME",
            "valueInUSD": 1
        }
    ]
        
obj = Pay()
# obj.airtime(turn_off_notification=False, country_to_send='Ghana', phone_number='254712345678', value_in_USD=3, sub_account='Antony Gakuru')
obj.chimoney(
    payment_details=pay_array_of_objects,   
)