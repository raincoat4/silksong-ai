from MaskDataset import MaskDataset
import torch
from torch.utils.data import DataLoader
from HealthCNN import HealthCNN

device = "cuda" if torch.cuda.is_available() else "cpu"

dataset = MaskDataset(
    csv_path="vision/testing_data/get_health/get_health_data_labels.csv",
    image_dir="vision/testing_data/get_health/photos"
)

test_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

model = HealthCNN()  
model.load_state_dict(torch.load("vision/models/health_cnn.pth"))
model.eval()
with torch.no_grad():
    images, labels = next(iter(test_loader))
    images = images.to(device)
    preds = model(images)
    predicted = preds.argmax(dim=1)

print("GT labels:", labels)
print("Predicted:", predicted.cpu())