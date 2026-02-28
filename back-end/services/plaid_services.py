import plaid
import time
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products 
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions

client_id = '69a3011352ca8e000ebb46fa'
secret = 'f6e227559ebed7d66430b477b5a0ac'

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def get_sandbox_access_token():
    options = SandboxPublicTokenCreateRequestOptions(
        override_username='user_transactions_dynamic',
        override_password='password'
    )
    sandbox_req = SandboxPublicTokenCreateRequest(
        institution_id='ins_109508', 
        initial_products=[Products('transactions')],
        options=options
    )
    
    public_token = client.sandbox_public_token_create(sandbox_req)['public_token']
    
    exchange_req = ItemPublicTokenExchangeRequest(public_token=public_token)
    access_token = client.item_public_token_exchange(exchange_req)['access_token']
    
    return access_token

access_token = get_sandbox_access_token()

time.sleep(5)

request = TransactionsSyncRequest(
    access_token=access_token,
)
response = client.transactions_sync(request)
transactions = response['added']

# the transactions in the response are paginated, so make multiple calls while incrementing the cursor to
# retrieve all transactions
while (response['has_more']):
    request = TransactionsSyncRequest(
        access_token=access_token,
        cursor=response['next_cursor']
    )
    response = client.transactions_sync(request)
    transactions += response['added']


parsed_data = []
income = 0
savings = 0
investing = 0
paying_debt = 0
total_spent = 0
budget_limit = 3000.00

for transaction in transactions:
    pfc = transaction.get('personal_finance_category')
    
    category_name = pfc['primary'] if pfc else 'Uncategorized'
    amount = transaction['amount']
    
    parsed_data.append({
        'amount': amount,
        'category': category_name
    })

    if amount < 0:
        income += abs(amount)
        
    elif category_name == 'LOAN_PAYMENTS':
        paying_debt += amount
        
    elif category_name == 'TRANSFER_OUT':
        savings += (amount * 0.5)
        investing += (amount * 0.5)
        
    elif amount > 0:
        total_spent += amount

not_overspending_score = budget_limit - total_spent

createDict = {
    "income": income,
    "savings": savings,
    "investing": investing,
    "paying_debt": paying_debt,
    "total_spent": total_spent,
    "not_overspending_score": not_overspending_score
}

print(createDict)
print(f"Success! Retrieved {len(transactions)} transactions.\n")

print(f"Income: ${income:.2f}")
print(f"Savings: ${savings:.2f}")
print(f"Investing: ${investing:.2f}")
print(f"Paying Debt: ${paying_debt:.2f}")
print(f"Remaining Budget: ${not_overspending_score:.2f}")
