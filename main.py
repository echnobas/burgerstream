#!/usr/bin/python3
import os
from flask import Flask

from config import *

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    if not os.path.exists(MEDIA_FOLDER):
        os.mkdir(MEDIA_FOLDER)

    from waitress import serve
    serve(app, host=HOST, port=PORT)
