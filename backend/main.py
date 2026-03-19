from fastapi import FastAPI, UploadFile, File
from PIL import Image
from analyzer import analyze_image

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    image = Image.open(file.file)
    scores = analyze_image(image)
    return scores