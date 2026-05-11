import torch.nn as nn
import torch.nn.functional as F

class MaskCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 8, 3, padding=1)
        self.conv2 = nn.Conv2d(8, 16, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        # forces output to fixed spatial size
        self.adaptive_pool = nn.AdaptiveAvgPool2d((5, 5))

        self.fc = nn.Linear(16 * 5 * 5, 6)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))

        # regardless of input size, output becomes [batch, 16, 5, 5]
        x = self.adaptive_pool(x)

        x = x.flatten(1)

        return self.fc(x)