from torch.utils.data import DataLoader
from archive.get_position.classes.PositionDataset import PositionDataset
import torch
import torch.nn as nn
from archive.get_position.classes.PositionCNN import PositionCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = PositionDataset(
    csv_path="vision/get_position/training_data/get_position_data_labels.csv",
    image_dir="vision/get_position/training_data/photos"
)

train_loader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=True
)

images, labels = next(iter(train_loader))
print(images.shape, labels)
print(len(train_loader))
model = PositionCNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(20):
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

torch.save(model.state_dict(), "position_cnn.pth")
