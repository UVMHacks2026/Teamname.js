import plaid
from plaid.api import plaid_api

# Available environments are
# 'Production'
# 'Sandbox'
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': '69a3011352ca8e000ebb46fa',
        'secret': 'f6e227559ebed7d66430b477b5a0ac59',
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)
