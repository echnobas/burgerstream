#!/usr/bin/python3
import os
import configparser
import base64
import random
import string
from flask import Flask

config = configparser.ConfigParser()
config.read("config.ini")

HOST = config["config"]["HOST"]
PORT = config["config"]["PORT"]
MEDIA_FOLDER = config["config"]["MEDIA_FOLDER"]
BURGER_PASSWORD = config["config"]["BURGER_PASSWORD"]
DEBUG = config["config"]["DEBUG"]

ydl_opts = {"format": "best[ext=mp4]",
            "noplaylist": "True",
            "extract_flat": "in_playlist",
            "outtmpl": MEDIA_FOLDER + "/%(title)s.mp4",
            "match-filters": "%(height)d >= %(width)d"}

app = Flask(__name__)


def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


BURGER_KEY = random_string(256)


if not os.path.exists(MEDIA_FOLDER):
    os.mkdir(MEDIA_FOLDER)

from routes import *

if __name__ == "__main__":
    from waitress import serve
    serve(app, host=HOST, port=PORT)
