# from chimopy.payout.pay import Pay
# from chimopy.mobile.transact import Transaction
from chimopy.auth import APIKey, APIUrl
from chimopy.info import Info
# from chimopy.accounts import Account, SubAccount
import os 
from dotenv import load_dotenv

load_dotenv()
chimoney_api_key = os.getenv('CHIMONEY_API_KEY', 'no key available')

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

bank_payout = [
    {
            "countryToSend": "Kenya",
            "account_bank": "044",
            "account_number": "0690000032",
            "valueInUSD": 10,
            "reference": "",
            "fullname" : "John Doe"
    }
]

airtime_payload = [
        {
            "countryToSend": "Kenya",
            "phoneNumber": "+254712345678",
            "valueInUSD": "5"
        },
        {
            "countryToSend": "Kenya",
            "phoneNumber": "+254787654321",
            "valueInUSD": "5"
        }
    ]
momos =  [
        {
            "countryToSend": "Kenya",
            "phoneNumber": "+254712345678",
            "valueInUSD": 3,
            "reference": "",
            "momoCode": "MPS"
        }
    ]
key = '66561c9cf6c6a7b1f0343c3b9a30cfc01aabe533ee093c73c8e9523a988b138f'
url ='https://chimoney-backend-api-sandbox.onrender.com'
APIKey, APIUrl = key, url
# obj = Pay(
#     api_key, api_url
#     )
# info = Info()
# response = obj.chimoney(
#     pay_array_of_objects
# )

# response = info.countries(
# )
# print(response.json())