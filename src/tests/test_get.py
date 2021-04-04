import json
#from src import db
from example.models import Cats
'''
def test_get_cat(test_app):
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
    for item in data:
         assert  item["name"] == "catty mcCatFace"
         assert  item["price"] == 5000
         assert  item["breed"] == "bengal"
'''

def test_all_cats(test_app, test_database, add_cat):
    add_cat("catty mcCatFace", 5000, "bengal")
    client = test_app.test_client()
    resp = client.get('/')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert  "catty mcCatFace" in  data[0]["name"]
    assert  5000 == data[0]["price"]
    assert "bengal" in  data[0]["breed"]
