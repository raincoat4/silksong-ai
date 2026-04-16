from torch.utils.data import Dataset
from PIL import Image
import pandas as pd
import torch
import os
from torchvision import transforms
import matplotlib.pyplot as plt

# inside position labels:
# 0 = tl = top left
# 1 = tc = top center
# 2 = tr = top right
# 3 = ml = middle left
# 4 = mc = middle center
# 5 = mr = middle right
# 6 = bl = bottom left
# 7 = bc = bottom center
# 8 = br = bottom right

class PositionDataset(Dataset):
    def __init__(self, csv_path, image_dir):
        self.data = pd.read_csv(csv_path)
        self.image_dir = image_dir
        self.transform = transforms.Compose([
            #maintain aspect ratio
            transforms.Resize((63,100)),
            transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.image_dir, self.data.iloc[idx]["image"])
        image = Image.open(img_path).convert("RGB")
        image = self.transform(image)

        # shows image
        # img_np = image.permute(1, 2, 0).numpy()
        # plt.imshow(img_np)
        # plt.axis('off')
        # plt.show()

        label = torch.tensor(self.data.iloc[idx]["position"], dtype=torch.long)
        return image, label