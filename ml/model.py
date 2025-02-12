from roboflow import Roboflow
import os


class Model():
    def __init__(self, version=4, confidence=33, overlap=15):
        self.version = version
        self.rf_client = Roboflow(api_key=os.environ.get("ROBOFLOW_API_KEY"))
        self.project = self.rf_client.workspace().project(os.environ.get("ROBOFLOW_PROJECT"))
        self.model = self.project.version(self.version).model
        self.confidence = confidence
        self.overlap = overlap
    
    def read_hand(image_path):
        """
        TODO: don't use path, differentiate from board
        """
        prediction = self.model.predict(image_path, confidence=self.confidence, overlap=self.overlap)
        output = {}
        for pred in prediction.json()['predictions']:
            output[pred["class"]] = f"{pred['confidence']*100:.2f}%"
        return output

    def read_board(image_path):
        """
        TODO: don't use path, differentiate from hand
        """
        prediction = self.model.predict(image_path, confidence=self.confidence, overlap=self.overlap)
        output = {}
        for pred in prediction.json()['predictions']:
            output[pred["class"]] = f"{pred['confidence']*100:.2f}%"
        return output