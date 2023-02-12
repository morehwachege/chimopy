# Usage
Chimopy methods return the response object as is. ```  ```

## Account
Example:

Getting transaction details by ```issueID```
``` python
    from chimopy.accounts.account import Account
    # api url
    obj = Account(api_key='key', api_url='url')
    obj.single_transaction(issue_d, sub_account)
```
All methods supported in Account
``` python
    details_by_issue_id(issue_id, sub_account='')
    all_transactions(sub_account='')
    single_transaction(id, sub_account='')
    transfer(receiver, amount, wallet, sub_account='' )
    delete_transaction(chi_ref, sub_account='')
```

All methods supported in SubAccount
``` python

    from chimopy.accounts.account import SubAccount
    # api url
    obj = SubAccount(api_key='key', api_url='url')
    obj.associated()
    obj.details(id)
    obj.delete(id)
    obj.create(name)
```