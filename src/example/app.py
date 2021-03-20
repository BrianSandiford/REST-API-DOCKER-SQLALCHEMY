import json
import os
import sys
from flask import request
from flask_restx import Resource, Api
from . import create_app, database
from .models import Cats

app = create_app()
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('example.config.DevelopmentConfig')  # new

#@app.route('/', methods=['GET'])
@api.route('/home')
class GetCats(Resource):
#def fetch():
 def get(self):
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


#@app.route('/add', methods=['POST'])
@api.route('/add')
class PutCats(Resource):
 def post(self):
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 201


#@app.route('/remove/<cat_id>', methods=['DELETE'])
@api.route('/remove/<cat_id>')
class RemoveCats(Resource):
 def delete(self,cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200

#@app.route('/edit/<cat_id>', methods=['PATCH'])
@api.route('/edit/<cat_id>')
class PatchCats(Resource):
 def patch(self,cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200

