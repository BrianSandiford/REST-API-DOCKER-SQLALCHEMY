import json

def test_add_cat(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/add',
        data=json.dumps({
            'name': 'catty mcCatFace',
            'price': 5000,
            'breed': 'bengal'
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'Added' in data

def test_add_cat_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/add',
        data=json.dumps({}),
        content_type='application/json',
    )
    assert resp.status_code == 400

def test_add_cat_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/add',
         data=json.dumps({
            'cost': 5000,
        }),
        content_type='application/json',
    )
    assert resp.status_code == 400
