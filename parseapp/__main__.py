import logging

DEFAULT_LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(level=DEFAULT_LOGGING_LEVEL)
logging.root.setLevel(DEFAULT_LOGGING_LEVEL)

from parseapp import app

if __name__ == '__main__':
    app.run(debug=True)
