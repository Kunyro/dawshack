from flask import Flask, flash, abort, redirect, render_template, request, url_for
from spotify_to_color import spotify_to_color

app = Flask(__name__)

@app.route("/")
def home():
    albums = spotify_to_color()
    print("THE ALBUMS", albums)
    return render_template('home.html', albums=albums)
