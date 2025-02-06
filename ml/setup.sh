#!/bin/bash -e

git submodule update --init --recursive
pip install -r yolov5/requirements.txt
pip install -r requirements.txt


