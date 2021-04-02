import json

from flask import request
from flask_expects_json import expects_json
from . import create_app, database
from .models import Cats

app = create_app()

schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'price': {'type': 'number'},
        'breed': {'type': 'string'}
    },
    'required': ['email', 'price', 'breed']
}




@app.route('/', methods=['GET'])
def fetch():
    cats = database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200


@app.route('/add', methods=['POST'])
@expects_json(schema)
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 201


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200
