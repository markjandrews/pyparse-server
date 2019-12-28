import os

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

config = {
    'database_uri': os.environ.get('DATABASE_URI', 'sqlite:///{}'.format(os.path.join(SCRIPT_DIR, '..', 'parseapp.db')))
}

__all__ = [config]
