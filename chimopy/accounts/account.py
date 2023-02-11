import requests


class Account:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'

    
    def details_by_issue_id(self, issue_id, sub_account=''):
        ''' Get transaction details by issue ID '''

        uri= f'{self.api_version}/accounts/issue-id-transactions?issueID={issue_id}'
        url= f'{self.api_url}/{uri}'
        payload = {}
        if sub_account != '':
            payload['subAccount'] = sub_account
        
        response = requests.post(url, headers=self.headers, json=payload)
        return response


    def all_transactions(self, sub_account=''):
        ''' Get all transactions '''

        uri= f'{self.api_version}/accounts/transactions'
        url= f'{self.api_url}/{uri}'
        payload={}
        if sub_account != '':
            payload['subAccount'] = sub_account
            
        response = requests.post(url, headers=self.headers, json=payload)
        return response
    

    def single_transaction(self, id, sub_account=''):
        ''' Get details about a single transactions using transaction id '''

        uri= f'{self.api_version}/accounts/transaction?id={id}'
        url= f'{self.api_url}/{uri}'
        payload={}
        if sub_account != '':
            payload['subAccount'] = sub_account
            
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    
    def transfer(self, receiver, amount, wallet, sub_account='' ):
        ''' Account Transfer '''
        uri= f'{self.api_version}/accounts/transfer'
        url= f'{self.api_url}/{uri}'
        payload = {
            'receiver': receiver,
            'amount': amount,
            'wallet': wallet
        }
        if sub_account != '':
            payload['subAccount'] = sub_account

        response = requests.post(url, headers=self.headers, json=payload)
        return response

    
    def delete_transaction(self, chi_ref, sub_account=''):
        uri= f'{self.api_version}/accounts/delete-unpaid-transaction?chiRef={chi_ref}'
        url= f'{self.api_url}/{uri}'
        if sub_account != '':
            url += f'&subAccount={sub_account}'

        response = requests.delete(url, headers=self.headers)
        return response

        
class SubAccount:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        self.api_version = 'v0.2'

    
    def create(self, name):
        ''' Create sub account '''

        uri= f'{self.api_version}/sub-account/create'
        url= f'{self.api_url}/{uri}'
        payload = {
            'name': name
        }
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    
    def delete(self, id):
        ''' Delete sub account using id '''
        uri= f'{self.api_version}/sub-account/delete'
        url= f'{self.api_url}/{uri}'
        payload = {
            'id': id
        }

        response = requests.delete(url, headers=self.headers, json=payload)
        return response


    def details(self, id):
        ''' Get details about a sub sccount '''

        uri= f'{self.api_version}/sub-account/get?id={id}'
        url= f'{self.api_url}/{uri}'
        response = requests.get(url, headers=self.headers, json=payload)

        return response

    
    def associated(self):
        ''' Get sub accounts associated with a user '''
        uri= f'{self.api_version}/sub-account/list'
        url= f'{self.api_url}/{uri}'

        response = requests.get(url, headers=self.headers)
        return response

