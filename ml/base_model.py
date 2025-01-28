import torch.nn as nn
from torchvision.datasets import ImageFolder
from consts import MODEL
import timm


# model for classification
class CardClassifierModel(nn.Module):
    def __init__(self, num_classes=53):
        super().__init__()

        # pre-trained EfficientNet model (may need to change model)
        self.base = timm.create_model(MODEL, pretrained=True)
        self.features = nn.Sequential(*list(self.base.children())[:-1])

        out_size = 1280
        self.classifier = nn.Sequential(nn.Flatten(), nn.Linear(out_size, num_classes))

    def forward(self, x):
        # Connect these parts and return the output
        x = self.features(x)
        output = self.classifier(x)
        return output
