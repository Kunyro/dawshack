from dominant_color.dominant_color import sort_images_by_color
from get_spotify import *


spotify = Get_spotify()

albums = spotify.get_random_album(spotify.token, 50, "album")

album_names = []
images = []
link = []
for album in albums:
    album_names.append(album["name"])
    images.append(album["image"])
    link.append(album["link_to_album"])

album_dict = {"images" : images, "link" : link}
covers_sorted = sort_images_by_color(albums)
