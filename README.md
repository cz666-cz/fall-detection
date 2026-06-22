CFD-YOLO: Fall Detection in Complex Scenes Based on Attention Mechanism and Feature Fusion 

Introduction

CFD-YOLO is an enhanced fall-detection framework built upon YOLO11. This model is designed to tackle the challenging task of detecting falls in real-world environments characterized by cluttered backgrounds, severe target occlusion, and a wide variability of fall postures. It successfully balances the need for fine-grained feature extraction of ambiguous postures with the stringent real-time requirements of edge device deployment.

Main Contributions
 
Boundary-Aware Slide Loss (BA-Slide Loss): A novel loss function that introduces an adaptive boundary-aware weighting mechanism. It focuses on ambiguous boundary samples (such as transitional postures between sitting, bending, crouching, and falling) by assigning them larger weights, thereby improving posture discrimination and reducing classification confusion.

Global Attention Mechanism (GAM): Integrated into the backbone network to establish global interactions across channels and spatial dimensions. This enhances the spatial-channel feature representation for complex human body postures, specifically targeting scattered limbs and torso features.

Wavelet-Enhanced C3k2_WT Module: Designed by integrating Wavelet Convolution (WTConv) into YOLO's C3k2 bottleneck structure. This module captures fine-grained motion features and frequency-domain information by separating low-frequency structural representations and high-frequency edge/texture details.

GSConv-Based Lightweight Neck: Tailored by removing the small-object detection layer and replacing standard convolutions with Group Shuffle Convolution (GSConv). This context-aware framework significantly reduces computational redundancy while improving the efficiency of multiscale feature fusion.
 

Performance

Extensive evaluations demonstrate that CFD-YOLO achieves an optimal balance between high detection accuracy and real-time inference speed. On the Roboflow Fall Detection dataset, CFD-YOLO achieves 96.6% mAP@50 and 75.4% mAP@50:95. Furthermore, on the Fall Computer Vision dataset, it attains 97.9% mAP@50 and 88.3% mAP@50:95. In addition to its high accuracy, the model maintains a low computational cost of just 7.1 GFLOPs. Deployment evaluations under FP32 precision also demonstrate impressive real-time inference speeds of 299 FPS on an NVIDIA RTX 4070 Ti, as well as 68.7 FPS and 51.3 FPS on a Jetson Orin Nano 8GB edge device operating under 25W and 15W power modes, respectively.

Requirements

The model was trained and evaluated using the following software environment:
Python: 3.9.20 
PyTorch: 2.6.0 (CUDA 12.4) 
Ultralytics: 8.3.63 


Dataset Preparation

Organize the dataset as follows:
datasets/
├── images
│   ├── train
│   ├── val
│   └── test
│
├── labels
│   ├── train
│   ├── val
│   └── test
│
└── data.yaml

Datasets used in this work:
Roboflow Fall Detection Dataset
Fall Computer Vision Dataset

Training Details

To reproduce the training results, the following hyperparameters and configurations were used:

Image Resolution: 640 
 
Epochs: 300  
Batch Size: 2 
Optimizer: Stochastic Gradient Descent (SGD)  
Initial Learning Rate: 0.01 
Random Seed: 42 
Workers (Data Loading): 1


Applications

CFD-YOLO can be applied to:
Elderly Care Monitoring
Smart Healthcare
Hospital Surveillance
Public Safety Monitoring
Campus Security
Industrial Safety Monitoring
Edge AI Vision Systems
