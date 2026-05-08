# 2D Game Vision AI Agent (Silksong)

A vision-based AI system that extracts structured game-state features from raw gameplay frames to enable autonomous gameplay.

## Features

- **CNN-based perception:** Detects character health, position, and movement from pixel data.  
- **Custom datasets:** Screenshots captured and labeled programmatically for supervised learning.  
- **GPU-accelerated training:** Efficient training using PyTorch and CUDA for real-time performance.  
- **Modular design:** Each feature (health, position, grounded state) is modeled independently for flexibility.

## Tech Stack

Python, PyTorch, OpenCV, NumPy, Pillow, torchvision

## important

if imports fail, might need to run pip install -e .

standing - 0, jumping - 1, moving right - 2, falling - 3, moving left - 4
## devlog

apr 28:
photos sort of working, need to edit window coords a bit
also for movement, just moving right, moving left, jumping, falling for now.
basic inputs to agent are movement and hp, do i need taking damage? maybe not for now