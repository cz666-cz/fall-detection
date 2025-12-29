CFD-YOLO: Fall Detection in Cluttered Backgrounds Based on YOLOv11

Paper: CFD-YOLO: Fall Detection in Cluttered Background with Global Attention and Wavelet Convolution
Task: Vision-based Human Fall Detection
Framework: YOLOv11 (Ultralytics)

Introduction

Human fall detection plays a crucial role in smart healthcare and elderly care systems.
However, accurate fall detection in real-world environments remains challenging due to cluttered backgrounds, occlusion, complex human postures, and diverse illumination conditions.

To address these challenges, we propose CFD-YOLO, an improved fall detection framework built upon YOLOv11.
The model enhances global contextual perception, multi-frequency feature representation, and difficult-sample learning while maintaining computational efficiency, making it suitable for real-time and resource-constrained scenarios.

Key Contributions

Global Attention Mechanism (GAM)
Enhances long-range spatial–channel interactions and improves robustness under occlusion and background clutter.

C3k2 WT Module with Wavelet Convolution
Introduces frequency-domain decomposition to jointly capture global posture structure and fine-grained edge details.

Slide Loss Function
Dynamically emphasizes hard boundary samples to improve detection accuracy in complex fall scenarios.

Lightweight Neck with GSConv
Removes redundant small-object detection heads and reduces computational cost while preserving multi-scale feature fusion.

Dedicated Fall Detection Framework
Tailored for complex, real-world fall detection scenarios with strong generalization ability.

Model Architecture

The overall architecture of CFD-YOLO is illustrated below:

Backbone (YOLO11 + GAM + C3k2 WT)
        ↓
Lightweight Neck (GSConv, Medium & Large Heads)
        ↓
Decoupled Detection Head


Please refer to Fig. 2 in the paper for the complete network architecture.

Datasets

Experiments are conducted on two public benchmark datasets:

1️⃣ Roboflow Fall Detection Dataset

Total images: 10,787

Split: 7,551 (train) / 2,157 (val) / 1,079 (test)

Scenarios: elderly care, surveillance, workplace safety, sports injuries

2️⃣ Fall Computer Vision Dataset

Total images: 2,716

Split: 1,901 (train) / 544 (val) / 271 (test)

Diverse indoor & outdoor environments with varied fall postures

Dataset format (YOLO style):

datasets/
├── images/
│   ├── train
│   ├── val
│   └── test
└── labels/
    ├── train
    ├── val
    └── test

⚙️ Environment Setup

Python 3.9

PyTorch 2.6.0

CUDA 12.4

Ultralytics 8.3.63

GPU: NVIDIA RTX 4070 Ti (12GB)

Install dependencies:

pip install -r requirements.txt

🚀 Training

Example training command:

python train.py \
  --model cfgs/CFD-YOLO.yaml \
  --data data/Roboflow.yaml \
  --epochs 300 \
  --img 640 \
  --batch 2


Key training settings:

Optimizer: SGD

Initial learning rate: 0.01

Epochs: 300

Random seed: 42

🔍 Evaluation

Run evaluation on the test set:

python val.py --weights runs/train/best.pt

Metrics

Precision (P)

Recall (R)

mAP@0.5

mAP@0.5:0.95

GFLOPs (computational cost)
