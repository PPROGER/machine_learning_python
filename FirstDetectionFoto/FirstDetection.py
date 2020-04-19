#!/usr/bin/python3
from imageai.Detection import ObjectDetection
import os


def FirstDetection(model_path, image_inp):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , str(model_path)))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , str(image_inp)), output_image_path=os.path.join(execution_path , "/home/pproger/Desktop/machine_learning_python/FirstDetectionFoto/imagenew.jpeg"))
    return detections
    

