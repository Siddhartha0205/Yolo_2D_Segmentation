from ultralytics import YOLO

model = YOLO('yolov8m_seg_custom.pt')

model.predict(source = "butterfly_video2.mp4", show = True, save = True, show_labels = True, show_conf = True, conf = 0.5, save_txt = False, save_crop = False, line_width = 2)