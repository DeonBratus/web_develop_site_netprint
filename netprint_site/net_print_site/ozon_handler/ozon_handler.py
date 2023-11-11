import requests


url = 'https://api-seller.ozon.ru/v3/posting/fbs/list'
client_id = "1322583"
api_key = "e6861620-9280-4432-9796-c23de7aa6a3f"
headers = {
    "Client-Id": client_id,
    "Api-Key": api_key
}

params = {

    "posting_number": "57195475-0050-3",
    "with": 

    {
        "analytics_data": false,
        "barcodes": false,
        "financial_data": false,
        "product_exemplars": false,
        "translit": false
    }

}

response = requests.get(url, headers=headers, json=params)
if response.status_code == 200:
    shipments = response.json()
    print(shipments)
else:
    print("Error:", response.status_code)