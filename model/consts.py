import torch

DATASET = "gpiosenka/cards-image-datasetclassification"
MODEL = "efficientnet_b0"
BATCH_SIZE = 32
SHUFFLE = True
LEARNING_RATE = 0.001
EPOCHS = 10
MODEL_PATH = "weights.pth"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
CLASS_MAPPING_PATH = "class_mapping.json"
