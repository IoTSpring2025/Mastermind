from roboflow import Roboflow
import os

rf = Roboflow(api_key=os.environ.get("ROBOFLOW_API_KEY"))
project = rf.workspace(os.environ.get("ROBOFLOW_WORKSPACE")).project(os.environ.get("ROBOFLOW_PROJECT"))
version = project.version(4)
dataset = version.download("yolov8")