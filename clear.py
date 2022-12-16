import cv2
import os

# Defining the path of the folder
path = './frames'

# Defining the function to detect the blurry images
def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

# Defining the function to delete the blurry images
def delete_blurry_images(path):
    for file in os.listdir(path):
        image = cv2.imread(os.path.join(path, file))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        if fm < 100:
            os.remove(os.path.join(path, file))

# Calling the function
delete_blurry_images(path)