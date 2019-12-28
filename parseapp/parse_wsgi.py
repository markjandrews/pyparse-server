import os
import sys

from parseapp import app as application

sys.path.insert(0, os.path.dirname(__file__))

__all__ = [application]
