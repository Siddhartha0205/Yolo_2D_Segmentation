from ultralytics import YOLO

model = YOLO('yolov8m_seg_custom.pt')

model.export(format = "onnx")

#model.export(format = "tflite")