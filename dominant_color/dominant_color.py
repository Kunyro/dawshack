# taken from tutorial here: https://www.youtube.com/watch?v=90s4SomOSa0
import cv2
import numpy as np
import os

# find dominant color in image using k-means clustering (3 by default)
def dominant_color(path):
    img = cv2.imread(os.path.join(path))

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

print(dominant_color('/Users/johakimfb/Code/dawshack/images/tank.jpg'))