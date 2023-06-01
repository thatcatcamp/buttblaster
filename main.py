from imageai.Classification.Custom import CustomImageClassification
from imageai.Detection import ObjectDetection
from imageai.Detection.Custom import CustomObjectDetection

import os

execution_path = os.getcwd()
"""
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolov3.pt"))
print(detector.CustomObjects())
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "4.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
exit(1)
"""
prediction = CustomImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "images", "models", "resnet50-images-test_acc_0.46154_epoch-1.pt"))
prediction.setJsonPath(os.path.join(execution_path, "images", "models", "images_model_classes.json"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "images/test/boobs/2bkl2um39jya1.jpg"), result_count=1)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "images/test/cats/50.jpg"), result_count=1)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "images/test/butt/m9kjy8i9nqxa1.jpg"), result_count=1)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

"""from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolov3.pt"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "images", "0.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")
"""
