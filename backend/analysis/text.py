import cv2
import numpy as np
import pytesseract

def text_score(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    h, w = img.shape

    boxes = pytesseract.image_to_boxes(img)

    if not boxes.strip():
        return 2.0  # assume bad if no text detected

    heights = []
    for line in boxes.splitlines():
        parts = line.split()
        if len(parts) < 5:  # skip malformed lines
            continue
        # b = [char, x1, y1, x2, y2]
        char, x1, y1, x2, y2 = parts[:5]
        heights.append(int(y2) - int(y1))

    if not heights:
        return 2.0  # if no valid boxes

    avg_height = np.mean(heights)

    # normalize based on image height
    ratio = avg_height / h
    score = ratio / 0.03 * 10
    score = min(max(score, 0), 10)

    return round(score, 1)