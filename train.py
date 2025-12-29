from ultralytics import YOLO



def main():
   
    model = YOLO(r"D:\Downloads\yolov12-main\yolov12-main\CFD-YOLO.yaml")

    model.train(
        data=r"D:\Downloads\yolov12-main\yolov12-main\ultralytics\cfg\datasets\Roboflow.yaml",
        epochs=300,
        seed=42,
        imgsz=640,
        batch=2,
        device=0,
        workers=1,
        augment=False, 
        name="RCFD-YOLO" 
    )



if __name__ == '__main__':
    main()
