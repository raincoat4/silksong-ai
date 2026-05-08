from torch.utils.data import DataLoader
from vision.CNNs.movementCNN.MovementDataset import MovementDataset 
import torch
import torch.nn as nn
from vision.CNNs.movementCNN.MovementCNN import MovementCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = MovementDataset(
    csv_path="vision/get_movement/training_data/labels.csv",
    image_dir="vision/get_movement/training_data/photos"
)

train_loader = DataLoader(
    dataset,
    batch_size=3,
    shuffle=True
)

images, labels = next(iter(train_loader))
print(images.shape, labels)

model = MovementCNN().to(device)

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

torch.save(model.state_dict(), "vision/models/movement_cnn.pth")
