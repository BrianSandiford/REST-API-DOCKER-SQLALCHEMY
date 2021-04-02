import json


def test_ping(test_app):
    client = test_app.test_client()
    resp0 = client.post(
        '/add',
        data=json.dumps({
            'name': 'catty mcCatFace',
            'price': 5000,
            'breed': 'bengal'
        }),
        content_type='application/json',
    ) 
    resp = client.get('/')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    data[0] == "bobby brown"
   # for item in data:
        # assert  item["name"] == "catty mcCatFace"
        # assert  item["price"] == 2000
        # assert  item["breed"] == "bengal"
