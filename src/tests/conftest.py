
import pytest

from example.app import app
from example.models import db
from example.models import Cats 

@pytest.fixture(scope='module')
def test_app():
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='function')
def add_cat():
    def _add_cat(name, price, breed):
        cat = Cats(name=name, price=price, breed=breed)
        db.session.add(cat)
        ad.session.commit()
        return cat
    return _add_user  
