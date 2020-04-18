#!/usr/bin/python3
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/image.jpeg"), output_image_path=os.path.join(execution_path , "/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/imagenew.jpeg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )