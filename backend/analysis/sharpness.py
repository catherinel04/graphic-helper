import cv2
import numpy as np

def sharpness_score(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    score = edges.sum() / edges.size
    return max(0,min(10,round(score, 1))) 