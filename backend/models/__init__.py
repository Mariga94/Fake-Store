#!/usr/bin/python3
from models.engine import db_storage
storage = db_storage.DBStorage()

storage.reload()