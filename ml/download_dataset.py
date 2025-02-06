from roboflow import Roboflow
import os
api_key = os.environ.get("ROBOFLOW_API_KEY")
workspace = os.environ.get("ROBOFLOW_WORKSPACE")
project = os.environ.get("ROBOFLOW_PROJECT")

rf = Roboflow(api_key=api_key)
project = rf.workspace(workspace).project(project)
version = project.version(3)
dataset = version.download("yolov5", location="dataset")

print("Dataset successfully downloaded.")