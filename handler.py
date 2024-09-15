from coinbase.rest import RESTClient
from json import dumps
import uuid

api_key = "api_key"
api_secret = "<api_secret>"
product_id = "BTC-USD"
dollar_amount = "<dollar amount>"
client_order_id = str(uuid.uuid4())

coinbase_client = RESTClient(api_key=api_key, api_secret=api_secret)

payload = {
  "client_order_id": client_order_id,
  "product_id": product_id,
  "side": "BUY",
  "order_configuration": {
    "market_market_ioc": {
      "quote_size": dollar_amount
    }
  }
}
order = coinbase_client.post(url_path="/api/v3/brokerage/orders", data=payload)
print(dumps(order, indent=2))