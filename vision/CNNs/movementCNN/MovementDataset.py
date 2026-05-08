from torch.utils.data import Dataset
from PIL import Image
import pandas as pd
import torch
import os
from torchvision import transforms

class MovementDataset(Dataset):
    def __init__(self, csv_path, image_dir):
        self.data = pd.read_csv(csv_path)
        self.image_dir = image_dir
        self.transform = transforms.ToTensor()

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.data.iloc[idx]["image"])
        image = Image.open(img_path).convert("RGB")
        image = self.transform(image)
        label = torch.tensor(self.data.iloc[idx]["movement"], dtype=torch.long)
        return image, label