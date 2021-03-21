import json


def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get('/home')
    data = json.loads(resp.data.decode())
#    assert resp.status_code == 200
    for item in data:
        if item[0] == 'price':
            assert  item["price"] == 5000
#    assert "catty mcCatFace" ==  data["name"]
#    assert 5000 in data['price']
~
