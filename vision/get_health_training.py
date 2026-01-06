from torch.utils.data import DataLoader
from MaskDataset import MaskDataset   # your file name
import torch
import torch.nn as nn
from HealthCNN import HealthCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = MaskDataset(
    csv_path="vision/training_data/get_health/get_health_data_labels.csv",
    image_dir="vision/training_data/get_health/photos"
)

train_loader = DataLoader(
    dataset,
    batch_size=3,
    shuffle=True
)

images, labels = next(iter(train_loader))
print(images.shape, labels)

model = HealthCNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(10):
    total_loss = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        preds = model(images)
        loss = criterion(preds, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}: loss = {total_loss / len(train_loader):.4f}")

