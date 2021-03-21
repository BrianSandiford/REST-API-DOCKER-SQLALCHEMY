import pytest

#from src import app, db
from example.models import db
from example.app import app

@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()