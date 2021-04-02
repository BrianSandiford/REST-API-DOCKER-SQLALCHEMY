import json


def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get('/')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    data[0] == "catty mcCatFace"
   # for item in data:
        # assert  item["name"] == "catty mcCatFace"
        # assert  item["price"] == 2000
        # assert  item["breed"] == "bengal"
