import cv2
import torch
import numpy as np
from torchvision import transforms
import matplotlib.pyplot as plt
from base_model import CardClassifierModel
import json
from consts import DEVICE, MODEL_PATH, CLASS_MAPPING_PATH
import io
import os


class CardClassifierMachine:
    def __init__(self):
        # load model, set to eval mode
        self.model = CardClassifierModel()
        print("DEVICE: ", DEVICE)
        if os.path.exists(MODEL_PATH):
            self.model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
        else:
            self.model.load_state_dict(torch.load("model/weights.pth", weights_only=True))
        self.model.to(DEVICE)
        self.model.eval()

        # load class mapping
        with open(CLASS_MAPPING_PATH) as class_json:
            self.class_map = json.load(class_json)

    def preprocess_image(self, image_path):
        image = cv2.imread(io.BytesIO(image_path))

        # rgb
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # model expects 128x128 image (may need to change)
        resized = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)

        # normalize - make sure we keep this the same as  the transform used for training. IMPORTANT
        transform = transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

        input_tensor = transform(resized)

        # unsqueeze to add the batch dimension - model expects 4D input (batch size, channels, height, width)
        return input_tensor.unsqueeze(0).to(DEVICE)

    def classify(self, image_path):
        image_tensor = self.preprocess_image(image_path)
        with torch.no_grad():
            output = self.model(image_tensor)

        # take softmax to get most probable class. this will need to change for when we predict multiple classes
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        predicted_class = torch.argmax(probabilities).item()

        # should we return the class number or word here?
        return self.class_map[str(predicted_class)], probabilities[
            predicted_class
        ].item()
