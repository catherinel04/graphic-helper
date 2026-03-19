import cv2
import numpy as np

def sharpness_score(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    score = laplacian_var / 1000 * 10
    score = min(max(score, 0), 10)

    return round(score, 1)