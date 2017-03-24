#!flask/bin/python

import os
from app import create_app
from app.models import User, Role
from config import config


app=create_app(config['default'])
app.run(debug=True)