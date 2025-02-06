from roboflow import Roboflow
import os

rf_key = os.environ.get("ROBOFLOW_API_KEY")
rf = Roboflow(api_key=rf_key)
project = rf.workspace().project(os.environ.get("ROBOFLOW_PROJECT"))
model = project.version(4).model
prediction = model.predict("test_image.png", confidence=33, overlap=15)


output = {}
for pred in prediction.json()['predictions']:
    output[pred["class"]] = f"{pred['confidence']*100:.2f}%"

print(output)
prediction.save("pred.jpeg")