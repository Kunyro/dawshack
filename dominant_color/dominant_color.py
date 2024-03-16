# taken from tutorial here: https://www.youtube.com/watch?v=90s4SomOSa0
import cv2
import numpy as np
import os
import urllib.request

# sort images by dominant color
# TODO implement the rgb sorting
def sort_images_by_color(url_list):
    url_rgb = {}
    for url in url_list:
        url_rgb[url] = dominant_color(url)

    sorted_url_rgb = sorted(url_rgb.items(), key=lambda x: x[1])
    return sorted_url_rgb

# find dominant color in image using k-means clustering (3 by default)
def dominant_color(url):
    # this is to transform the url to an img for cv2
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'

    height, width, _ = np.shape(img)
    print("Height: ", height, "\tWidth: ", width, "\n")

    data = np.reshape(img, (height * width, 3))
    data = np.float32(data)

    num_clusters = 3
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, num_clusters, None, criteria, 20, flags)
    print("Centers", "\n", centers)

    bars = []
    rgb_values = []
    
    for i, row in enumerate(centers):
        bar, rgb = create_bar(200, 200, row)
        bars.append(bar)
        rgb_values.append(rgb)

    img_bar = np.hstack(bars)

    cv2.imshow('Image', img)
    cv2.imshow('Dominant Colors', img_bar)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rgb_values

# create bar for dominant color visualization
def create_bar(height, width, color):
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    print("Red: ", red, "\tGreen: ", green, "\tBlue: ", blue, "\n")

    return bar, (red, green, blue)

#print(dominant_color('https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/1a/c2/1a/1ac21a9d-3ffd-3f80-dc96-223622b50b5f/Madvillainy.jpg/600x600bb.jpg'))

print(sort_images_by_color([
    'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/1a/c2/1a/1ac21a9d-3ffd-3f80-dc96-223622b50b5f/Madvillainy.jpg/600x600bb.jpg',
    'https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228',
    'https://i.ytimg.com/vi/SxgsofgCjFQ/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgBzgWAAtAFigIMCAAQARh_IB8oEzAP&rs=AOn4CLATEtVInjnXoK2W8WNsjKexe3iQuQ'
    ]))