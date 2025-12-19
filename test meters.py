import warnings
import torch
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolo11GAM.yaml')

    model.info(detailed=True)
    try:
        model.profile(imgsz=[640,640])
    except Exception as e:
        print(e)
        pass
    model.fuse()