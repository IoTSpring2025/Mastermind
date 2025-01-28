#!/bin/bash -e
base_path=$PWD/test_images
img_path=${base_path}/IMG_2204.png
echo "Trying to upload: $img_path"

# Verify the file exists and is readable
if [ ! -f "$img_path" ]; then
  echo "Error: File not found: $img_path"
  echo "Possible files: " && ls $base_path
  exit 1
fi
curl -X POST -F image=@$img_path http://localhost:80/predict


