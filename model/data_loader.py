import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import kagglehub
from consts import DATASET
import os

class CardDataset(Dataset):
    def __init__(self, transform=None):
        self.path = kagglehub.dataset_download(DATASET)
        print("Dataset downloaded to:", self.path)

        self.transform = transform or transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ])

        # Load datasets
        self.data = ImageFolder(self.path, transform=self.transform)
        self.train_data = ImageFolder(os.path.join(self.path, "train"), transform=self.transform)
        self.val_data = ImageFolder(os.path.join(self.path, "valid"), transform=self.transform)
        self.test_data = ImageFolder(os.path.join(self.path, "test"), transform=self.transform)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]
    
    @property
    def classes(self):
        return self.data.classes
    
    @property
    def train(self):
        return self.train_data

    @property
    def val(self):
        return self.val_data

    @property
    def test(self):
        return self.test_data
