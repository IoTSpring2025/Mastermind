from roboflow import Roboflow
import os

class RoboflowClient():

    def __init__(self):
        self.api_key = os.environ.get("ROBOFLOW_API_KEY")
        self.workspace = os.environ.get("ROBOFLOW_WORKSPACE")
        self.project = os.environ.get("ROBOFLOW_PROJECT")
        self.rf = Roboflow(api_key=self.api_key)
        self.project = self.rf.workspace(self.workspace).project(self.project)
        self.version = self.project.version(3)

    def download_dataset(self):
        dataset = self.version.download("yolov5", location="dataset")
        print("Dataset successfully downloaded.")
        return dataset

    def upload_dataset(self, dataset):
        self.version.upload(dataset, name="yolov5")
        print("Dataset successfully uploaded.")

    def get_dataset(self):
        return self.version