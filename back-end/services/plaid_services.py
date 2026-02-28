import plaid
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products 

client_id = '69a3011352ca8e000ebb46fa'
secret = 'f6e227559ebed7d66430b477b5a0ac59'

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
    sandbox_req = SandboxPublicTokenCreateRequest(
        institution_id='ins_109508', 
        initial_products=[Products('transactions')]
    )
    
    # Using dictionary access for the response is safer in the newer Plaid SDK
    public_token = client.sandbox_public_token_create(sandbox_req)['public_token']
    
    exchange_req = ItemPublicTokenExchangeRequest(public_token=public_token)
    access_token = client.item_public_token_exchange(exchange_req)['access_token']
    
    return access_token

access_token = get_sandbox_access_token()

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

print(f"Success! Retrieved {len(transactions)} transactions.")