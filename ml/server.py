from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import io
from classifier import CardClassifierMachine
import os
import torch
import uvicorn
import cv2

# web server
server = FastAPI()
classifier = CardClassifierMachine()


@server.post("/predict")
async def predict(image: UploadFile = File(...)):
    # run inference
    img_contents = await image.read()
    np_image = np.frombuffer(img_contents, np.uint8)
    image_decoded = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    predicted_class, prob = classifier.classify(image_decoded)

    return JSONResponse({"class": predicted_class, "probability": prob})


if __name__ == "__main__":
    uvicorn.run(server, host="0.0.0.0", port=80)
