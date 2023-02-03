import configparser, string, random

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

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


BURGER_KEY = random_string(256)