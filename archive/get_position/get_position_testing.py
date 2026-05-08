from archive.get_position.classes.PositionDataset import PositionDataset
import torch
from torch.utils.data import DataLoader
from archive.get_position.classes.PositionCNN import PositionCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = PositionDataset(
    csv_path="vision/get_position/training_data/get_position_data_labels.csv",
    image_dir="vision/get_position/training_data/photos"
)

test_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

model = PositionCNN()  
model.load_state_dict(torch.load("vision/models/position_cnn.pth"))
model.eval()
with torch.no_grad():
    images, labels = next(iter(test_loader))
    images = images.to(device)
    preds = model(images)
    predicted = preds.argmax(dim=1)
#print(preds)
print("GT labels:", labels)
print("Predicted:", predicted.cpu())