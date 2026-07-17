 CFD-YOLO

 Fall Detection in Complex Scenes Based on Attention Mechanism and Feature Fusion

📌 Overview

Human fall detection plays an important role in intelligent surveillance, elderly care, and safety monitoring systems. However, detecting falls in real-world environments remains challenging due to complex backgrounds, severe occlusion, diverse human postures, illumination variations, and ambiguous transitional states.

In this work, we propose CFD-YOLO, an enhanced fall detection framework based on YOLO11, aiming to improve robustness and detection accuracy in complex scenarios while maintaining real-time inference capability.

CFD-YOLO introduces several task-oriented improvements:

- Boundary-Aware Slide Loss (BA-Slide Loss)  
  A novel loss optimization strategy designed to emphasize ambiguous samples near the IoU decision boundary and improve discrimination between fall and non-fall behaviors.

- Wavelet-enhanced C3k2_WT Module  
  A feature extraction module integrating wavelet transform and convolution operations to jointly exploit spatial-domain and frequency-domain information.

- Global Attention Mechanism (GAM)  
  An attention enhancement strategy incorporated into the backbone network to strengthen spatial-channel feature representation.

- Adaptive Multi-Scale Feature Fusion (AMSF)  
  A multi-scale feature fusion module deployed in the neck network to adaptively aggregate contextual information from different receptive fields.


Extensive experiments demonstrate that CFD-YOLO achieves superior performance compared with mainstream YOLO variants, CNN-based detectors, Transformer-based detectors, and state-space-model-based detectors.

The inference pipeline contains four stages:
1. Image preprocessing
2. Backbone feature extraction
3. Multi-scale feature fusion
4. Detection post-processing

🔥 Main Contributions

 1. Boundary-Aware Slide Loss (BA-Slide Loss)
Traditional Slide Loss mainly focuses on low-IoU hard samples.
However, in fall detection tasks, many challenging samples occur near the decision boundary:
- sitting vs. falling
- bending vs. falling
- partially occluded falling posture
To address this issue, BA-Slide Loss introduces an adaptive boundary-aware weighting mechanism.
 Advantages:
- Enhances difficult sample learning
- Improves posture discrimination
- Provides stronger optimization signals
- Improves localization accuracy


 2. Wavelet-enhanced C3k2_WT Module


The proposed C3k2_WT module integrates Wavelet Transform Convolution (WTConv) into the C3k2 structure.

The input feature is decomposed into four frequency components:

          Input Feature

                |
                ↓

      Discrete Wavelet Transform

    --
    |      |      |      |
    LL     LH     HL     HH

    Low   Edge   Edge   Texture
    Frequency Details


The module simultaneously captures:
- Global structural information
- Local texture details
- Fine-grained human posture features


 3. Global Attention Mechanism (GAM)
GAM is integrated into the backbone network to enhance global contextual modeling.
It improves:
- Channel dependency learning
- Spatial feature interaction
- Human body representation
Compared with conventional attention modules, GAM preserves complete feature dimensions and strengthens cross-dimensional interactions.




 4. Adaptive Multi-Scale Feature Fusion (AMSF)
AMSF is introduced into the neck network.
The module adopts:
- 3×3 depthwise convolution
- 5×5 depthwise convolution
- 7×7 depthwise convolution
A selective-kernel inspired attention mechanism is employed to dynamically adjust contributions from different receptive fields.
Advantages:
- Adaptive contextual aggregation
- Improved semantic representation
- Reduced redundant computation



📊 Experimental Results


CFD-YOLO was extensively evaluated on two public fall detection datasets, including the Roboflow Fall Detection Dataset and the Fall Computer Vision Dataset.

On the Roboflow Fall Detection Dataset, CFD-YOLO achieves a Precision of 93.7%, Recall of 92.8%, mAP@50 of 97.2%, and mAP@50:95 of 75.4%, significantly outperforming the baseline YOLO11n. Compared with YOLO11n, CFD-YOLO improves mAP@50 by 4.5 percentage points and mAP@50:95 by 8.8 percentage points, demonstrating stronger robustness in complex scenarios involving occlusion, cluttered backgrounds, and diverse human postures.

On the Fall Computer Vision Dataset, CFD-YOLO further achieves a Precision of 96.6%, Recall of 93.9%, mAP@50 of 98.2%, and mAP@50:95 of 88.6%, validating its strong generalization capability across different environments and fall patterns.

In terms of computational efficiency, CFD-YOLO achieves 322.89 FPS with only 3.10 ms latency on an NVIDIA RTX 4070 Ti GPU. Furthermore, deployment experiments on the NVIDIA Jetson Orin Nano 8GB edge device demonstrate real-time performance, reaching 68.4 FPS at 25W power mode and 50.8 FPS at 15W power mode.

Extensive comparisons with CNN-based detectors, Transformer-based detectors, State Space Model-based detectors, and other YOLO variants demonstrate that CFD-YOLO achieves an effective balance between detection accuracy, computational efficiency, and real-time deployment capability.

🌍 Application Scenarios


CFD-YOLO is designed for real-world fall detection applications where reliable and timely human fall recognition is required. Its robustness under complex backgrounds, occlusion, and diverse human postures makes it suitable for various intelligent monitoring scenarios.

 1. Elderly Care and Smart Healthcare

Falls are one of the major safety risks for elderly individuals. CFD-YOLO can be integrated into smart cameras and healthcare monitoring systems to automatically detect accidental falls in:
- Nursing homes
- Assisted living facilities
- Hospital wards
- Home care environments
The system can provide timely alerts to caregivers and medical personnel, reducing response time after a fall event.

 2. Intelligent Surveillance Systems

Traditional surveillance systems mainly rely on manual monitoring, which is inefficient for continuous safety supervision.
CFD-YOLO can enhance intelligent surveillance platforms by automatically identifying fall events in:
- Public areas
- Residential communities
- Shopping malls
- Transportation hubs
Its ability to handle cluttered scenes and partial occlusion enables reliable detection in crowded environments.


 3. Smart Campus Safety Monitoring

Students and elderly people may experience sudden falls in educational environments.
CFD-YOLO can be applied in:
- Schools
- Universities
- Dormitories
- Campus public spaces
The model can assist safety management systems by detecting abnormal fall events and providing rapid emergency notifications.

 4. Public Transportation and Crowded Environments

Falls frequently occur in crowded areas where human bodies may be partially blocked by surrounding people or objects.
Potential applications include:
- Bus stations
- Subway stations
- Airports
- Railway platforms
CFD-YOLO's enhanced feature representation improves detection reliability under occlusion and complex backgrounds.

 5. Industrial and Workplace Safety Monitoring

In industrial environments, worker falls may lead to serious injuries.
CFD-YOLO can support safety monitoring in:
- Manufacturing factories
- Construction sites
- Warehouses
- Mining environments
Combined with existing surveillance cameras, the system can provide automatic accident detection and emergency response.

 6. Edge-Based Real-Time Monitoring Devices

Due to its efficient inference capability, CFD-YOLO can be deployed on edge computing platforms such as NVIDIA Jetson Orin Nano.
Potential applications include:
- Smart cameras
- Mobile monitoring robots
- Embedded safety devices
- IoT-based surveillance systems
The edge deployment capability enables real-time fall detection without requiring continuous cloud computing.
