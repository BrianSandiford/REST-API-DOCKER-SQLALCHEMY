import json
from example.models import Cats

def test_get_cats(test_app, test_database, add_cat):
    test_database.session.query(Cats).delete() #remove all rows in table before test
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

def test_remove_cats(test_app, test_database, add_cat):
    test_database.session.query(Cats).delete()
    cat =  add_cat("catty mcCatFace", 5000, "bengal")
    client = test_app.test_client()
    resp_one = client.get('/')
    data = json.loads(resp_one.data.decode())
    assert resp_one.status_code == 200
    assert len(data) == 1

    resp_two = client.delete(f"/remove/{cat.id}")
    data = json.loads(resp_two.data.decode())
    assert resp_two.status_code == 200
    assert "Deleted" in data  
 
    resp_three = client.get('/')
    data = json.loads(resp_three.data.decode())
    assert resp_three.status_code == 200
    assert len(data) == 0


def test_remove_invalid_cat(test_app, test_database):
    client = test_app.test_client()
    resp = client.delete("/remove/1024")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "Cat does not exist"  in data

def test_edit_cats(test_app, test_database, add_cat):
    cat =  add_cat("catty mcCatFace", 5000, "bengal")
    client = test_app.test_client()
    resp_one = client.patch(
             f"/edit/{cat.id}",
             data=json.dumps({
                  'name': 'catty mcCatFace',
                  'price': 1234567,
                  'breed': 'bengal'
             }),
             content_type='application/json',
   )
    data = json.loads(resp_one.data.decode())
    assert resp_one.status_code == 200
    assert "Edited" in data   

def test_edit_invalid_cats(test_app, test_database, add_cat):
    client = test_app.test_client()
    resp = client.patch(
             "/edit/1",
             data=json.dumps({ }),
             content_type='application/json',
   )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400

def test_edit_cats_does_not_exist(test_app, test_database, add_cat):
    client = test_app.test_client()
    resp = client.patch(
           "/edit/1024",
           data=json.dumps({
                  'name': 'catty mcCatFace',
                  'price': 1234567,
                  'breed': 'bengal'
           }),
           content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code ==  404
    assert "Cat does not exist" in data
