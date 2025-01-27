from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import io
from model.classifier import CardClassifierMachine
import os
import torch 

server = FastAPI()
gpu_enabled = torch.cuda.is_available()
classifier = CardClassifierMachine()

@server.post("/predict")
async def predict(image: UploadFile = File(...)):
    # read image file
    contents = await image.read()

    # run inference
    predicted_class, prob = classifier.classify(contents)

    return JSONResponse({"class": predicted_class, "probability": prob})
