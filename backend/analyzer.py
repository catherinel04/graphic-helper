from analysis.color import color_score
from analysis.sharpness import sharpness_score
from analysis.text import text_score
from analysis.composition import composition_score

def analyze_image(image):
    scores = {
        "color": color_score(image),
        "sharpness": sharpness_score(image),
        "text": text_score(image),
        "composition": composition_score(image),
    }

    # overall score
    overall = (
        scores["color"] * 0.25 +
        scores["sharpness"] * 0.2 +
        scores["text"] * 0.25 +
        scores["composition"] * 0.3
    )

    scores["overall"] = round(overall, 1)
    return scores