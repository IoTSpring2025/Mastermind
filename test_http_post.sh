#!/bin/bash -e

curl -X POST -F "image=@ml/test_images/IMG_2204.png" http://0.0.0.0:80/predict


