from ultralytics import YOLO



def main():
    # 使用绝对路径加载模型配置文件，训练之前记得注释掉损失函数
    model = YOLO(r"D:\Downloads\yolov12-main\yolov12-main\LHFD-YOLO.yaml")

    # 开始训练
    model.train(
        data=r"D:\Downloads\yolov12-main\yolov12-main\ultralytics\cfg\datasets\Traffic accident FW.yaml",
        epochs=300,
        seed=42,
        imgsz=640,
        batch=2,
        device=0,
        workers=1,
        augment=False,  # 禁用图像增强
        name="TFLHFD"  # 设置训练运行名称
    )



if __name__ == '__main__':
    main()
