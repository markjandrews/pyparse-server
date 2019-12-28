import logging

from parseapp import app

log = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
