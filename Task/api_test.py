import allure
import pytest
import requests
import json
import base64

url = "https://api-sandbox.dev.tnxhub.com/v1/checkout/pay"

payload = json.dumps({
    "reference": "id23422",
    "order_id": "12345",
    "order_description": "some test order",
    "amount": "100",
    "currency": "USD",
    "result_url": "https://my.site/order",
    "success_url": "https://my.site/order/deposit-success",
    "error_url": "https://my.site/order/error",
    "language": "EN",
    "customer_token": "b123cd4533523a412e2",
    "allow_currency_convert": False,
    "forced_convert": False,
    "allow_cascading_after_3ds": False,
    "callback_url": "https://my.site/order/cb"
})

credentials = 'pk_5qA8Ok4FSSaenYkqqCbUhX09Il0njoyQ:sk_DOrmIpVxxKYinPQgGNH9BiTPImsipiSr'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

headers = {
    'Content-type': 'application/json',
    'Authorization': f'Basic {encoded_credentials}'
}

response = requests.request("POST", url, headers=headers, data=payload)
response_data = response.json()

print(response_data)

@allure.feature("FEATURE_2")
@allure.story("STORY_2")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_reason():
    if response_data.get("reason") == "Ok":
        print("The reason is Ok.")
    else:
        print("The reason is not Ok. Reason:", response_data.get("reason"))