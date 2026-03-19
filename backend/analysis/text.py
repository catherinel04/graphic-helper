import cv2
import numpy as np
import pytesseract

def text_score(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    h, w = img.shape

    boxes = pytesseract.image_to_boxes(img)

    if len(boxes) == 0:
        return 2.0  # assume bad if no text detected

    heights = []
    for b in boxes:
        b = b.split()
        heights.append(int(b[3]) - int(b[1]))

    avg_height = np.mean(heights)

    # normalize based on image size
    ratio = avg_height / h

    score = ratio / 0.03 * 10
    score = min(max(score, 0), 10)

    return round(score, 1)