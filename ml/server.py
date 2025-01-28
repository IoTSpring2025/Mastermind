from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import io
from classifier import CardClassifierMachine
import os
import torch 

# web server
server = FastAPI()
classifier = CardClassifierMachine()

@server.post("/predict")
async def predict(image: UploadFile = File(...)):

    print(image)
    print(type(image))
    # read image file
    contents = await image.read()

    # run inference
    predicted_class, prob = classifier.classify(contents)

    return JSONResponse({"class": predicted_class, "probability": prob})
