from vision.CNNs.movementCNN.MovementDataset import MovementDataset
import torch
from torch.utils.data import DataLoader
from vision.CNNs.movementCNN.MovementCNN import MovementCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = MovementDataset(
    csv_path="vision/get_movement/testing_data/labels.csv",
    image_dir="vision/get_movement/testing_data/photos"
)
test_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

model = MovementCNN()  
model.load_state_dict(torch.load("vision/models/movement_cnn.pth"))
model.eval()
with torch.no_grad():
    images, labels = next(iter(test_loader))
    images = images.to(device)
    preds = model(images)
    predicted = preds.argmax(dim=1)

print("GT labels:", labels)
print("Predicted:", predicted.cpu())