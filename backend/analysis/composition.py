import cv2
import numpy as np

def composition_score(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    h, w = img.shape

    # ---- Rule of thirds ----
    third_w, third_h = w // 3, h // 3
    targets = [(third_w, third_h), (2*third_w, third_h),
               (third_w, 2*third_h), (2*third_w, 2*third_h)]

    aligned = 0

    for c in contours:
        M = cv2.moments(c)
        if M["m00"] == 0:
            continue
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        if any(abs(cx-x) < w*0.05 and abs(cy-y) < h*0.05 for x,y in targets):
            aligned += 1

    rule_score = min((aligned / max(len(contours), 1)) * 10, 10)

    # ---- Negative space ----
    filled = np.count_nonzero(edges)
    total = h * w
    neg_ratio = (total - filled) / total

    space_score = neg_ratio * 10

    # ---- Combine ----
    score = 0.5 * rule_score + 0.5 * space_score
    score = min(max(score, 0), 10)

    return round(score, 1)