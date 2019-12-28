import importlib.util
import logging
import os
import sys

from flask import Flask
from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))


log = logging.getLogger(__name__)

app = Flask(__name__)

config_path = os.environ.get('PARSE_CONFIG', os.path.join(SCRIPT_DIR, 'config.py'))
config_name = 'parseapp.config'

spec = importlib.util.spec_from_file_location(config_name, config_path)
module = importlib.util.module_from_spec(spec)
sys.modules[config_name] = module
spec.loader.exec_module(module)

config = getattr(module, 'config')

engine = create_engine(config['database_uri'], convert_unicode=True, echo=True)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = flask_scoped_session(session_factory, app)

#
# meta = MetaData()
# tbl = Table('Testing', meta,
#             Column('id', Integer, primary_key=True),
#             Column('name', String(50)),
#             Column('lastname', String(50)))
# meta.create_all(engine)

from parseapp import routes
