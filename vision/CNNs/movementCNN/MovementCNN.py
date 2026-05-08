import torch.nn as nn
import torch.nn.functional as F

class MovementCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 8, 3, padding=1)
        self.conv2 = nn.Conv2d(8, 16, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        self.global_pool = nn.AdaptiveAvgPool2d((5, 5))

        self.fc = nn.Linear(16 * 5 * 5, 5) #output

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        x = self.global_pool(x)   
        x = x.view(x.size(0), -1)
        return self.fc(x)