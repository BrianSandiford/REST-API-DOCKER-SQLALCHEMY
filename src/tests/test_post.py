import json


def test_add_user(test_app, test_database):
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
