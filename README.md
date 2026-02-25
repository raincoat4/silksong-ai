# 2D Game Vision AI Agent (Silksong)

A vision-based AI system that extracts structured game-state features from raw gameplay frames to enable autonomous gameplay.

## Features

- **CNN-based perception:** Detects character health, position, and movement from pixel data.  
- **Custom datasets:** Screenshots captured and labeled programmatically for supervised learning.  
- **GPU-accelerated training:** Efficient training using PyTorch and CUDA for real-time performance.  
- **Modular design:** Each feature (health, position, grounded state) is modeled independently for flexibility.

## Tech Stack

Python, PyTorch, OpenCV, NumPy, Pillow, torchvision

