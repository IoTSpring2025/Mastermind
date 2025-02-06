#!/bin/bash -e

# check if COMET_API_KEY is set
if [ -z "$COMET_API_KEY" ]; then
  echo "COMET_API_KEY is not set"
  exit 1
fi

# check if dataset/ is empty
if [ ! "$(ls -A /content/drive/MyDrive/iot/dataset)" ]; then
  python3 download_dataset.py
fi

# check if weights are available
if [ ! -f /content/drive/MyDrive/iot/weights/yolov8s.pt ]; then
  python3 download_weights.py
fi

yolo task=detect mode=train model=yolov8s.pt data=/content/drive/MyDrive/iot/dataset/data.yaml epochs=100 imgsz=640 device=0