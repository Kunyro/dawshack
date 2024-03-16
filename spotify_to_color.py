import time
from dominant_color.dominant_color import sort_images_by_color
from get_spotify import *

def spotify_to_color():
    spotify = Get_spotify()

    albums = spotify.get_random_album(spotify.token, 50, "album")
    #time.sleep(10)
    covers_sorted = sort_images_by_color(albums)

    return covers_sorted
