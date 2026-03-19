import cv2
import numpy as np

def color_score(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2LAB)
    L = img[:, :, 0]  # brightness channel

    contrast = np.std(L)

    # normalize to 0–10
    score = contrast / 25
    score = min(max(score, 0), 10)

    return round(score, 1)