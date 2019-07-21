import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = r"C:\Users\Jwp\Desktop\workspace\python\Project\Machine_Learning\CNN\ImageNet\dataset\kagglecatsanddogs_3367a\PetImages"
CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  # path to cats or dogs dir
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        # plt.imshow(img_array, cmap="gray")
        # plt.show()
        break
    break

print(img_array)