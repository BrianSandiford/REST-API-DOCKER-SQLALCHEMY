import json
from example.models import Cats

def test_all_cats(test_app, test_database, add_cat):
    add_cat("catty mcCatFace", 5000, "bengal")
    add_cat("Fluff", 4000, "Siamese")
    client = test_app.test_client()
    resp = client.get('/')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data) == 2
    assert  "catty mcCatFace" in  data[0]["name"]
    assert  5000 == data[0]["price"]
    assert "bengal" in  data[0]["breed"]
    assert  "Fluff" in  data[1]["name"]
    assert  4000 == data[1]["price"]
    assert "Siamese" in  data[1]["breed"]

