#!/bin/sh

python start.py db init
python start.py db migrate
python start.py db upgrade

python start.py runserver --host 0.0.0.0
