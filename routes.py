import os
from flask import render_template, send_from_directory, request
from yt_dlp import YoutubeDL

from main import app, BURGER_KEY
from config import HOST, PORT, MEDIA_FOLDER, BURGER_PASSWORD, BURGER_KEY, DEBUG, ydl_opts

def getMedia():
    media = os.listdir(MEDIA_FOLDER)
    return media

@app.route("/", methods=("GET", "POST"))
def main():
    return render_template("main.html", sitename=request.url)


@app.route("/api/v1/getkey/password=<password>", methods=("GET", "POST"))
def api_get_key(password):
    if str(password) == BURGER_PASSWORD or DEBUG == "true":
        return {
            "error": None,
            "results": {
                "key": BURGER_KEY}
        }
    else:
        return {
            "error": "Incorrect password"
        }, 403


@app.route("/api/v1/list", methods=("GET", "POST"))
def api_list():
    key = request.headers.get("x-burger-auth")
    if key == BURGER_KEY or DEBUG == "true":
        return {
            "error": None,
            "results": getMedia()
        }
    else:
        return {
            "error": "Incorrect key"
        }, 403


@app.route("/api/v1/get/filename=<filename>", methods=("GET", "POST"))
def api_get(filename):
    key = request.headers.get("x-burger-auth")
    if key == BURGER_KEY or DEBUG == "true":
        if os.path.exists(os.path.join(MEDIA_FOLDER, filename)):
            return send_from_directory(MEDIA_FOLDER, filename)
        else:
            return {
                "error": "File does not exist"
            }
    else:
        return {
            "error": "Incorrect key"
        }, 403


@app.route("/api/v1/download/url=<url>", methods=("GET", "POST"))
def api_download(url):
    key = request.headers.get("x-burger-auth")
    if key == BURGER_KEY or DEBUG == "true":
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return info
    else:
        return {
            "error": "Incorrect key"
        }, 403