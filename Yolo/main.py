from ultralytics import YOLO

model = YOLO('yolov8m.pt')
results = model('People.mp4', save=True)