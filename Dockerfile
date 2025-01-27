# container for cloud server
FROM python:3.12-slim

# install system dependencies for OpenCV 
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# copy model and server folders over
COPY model /app/model
COPY server /app/server

# run the server on port 80
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "80"]