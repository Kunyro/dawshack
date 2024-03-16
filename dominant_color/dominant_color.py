# taken from tutorial here: https://www.youtube.com/watch?v=90s4SomOSa0
import cv2
import numpy as np
import os
import urllib.request

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
    compactness, labels, centers = cv2.kmeans(data, num_clusters, None, criteria, 10, flags)
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

print(dominant_color('https://i.scdn.co/image/ab67616d00001e02ff9ca10b55ce82ae553c8228'))