import os
import signal
import time
import pyttsx3
import cv2
from imageai.Classification.Custom import CustomImageClassification
from loguru import logger
execution_path = os.getcwd()
RAMDISK = "/tmp/swap.jpg"
execution_path = os.getcwd()
prediction = CustomImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "images", "models", "resnet50-images-test_acc_0.76923_epoch-82.pt"))
prediction.setJsonPath(os.path.join(execution_path, "images", "models", "images_model_classes.json"))
prediction.loadModel()

engine = pyttsx3.init()

def signal_handler(sig, frame):
    """
    closes camera correctly on stop so we don't have to unplug it
    :param sig:
    :param frame:
    :return:
    """
    print('You pressed Ctrl+C!')
    camera.release()


logger.info("init")
signal.signal(signal.SIGINT, signal_handler)
camera = cv2.VideoCapture(1)
if not camera.isOpened():
    print("Cannot open camera")
    exit()
# CAP_PROP_FPS doesn't work for this - use sleep
while True:
    ret, frame = camera.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imwrite(RAMDISK, frame)
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, RAMDISK), result_count=1)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        if eachPrediction == "boobs":
            engine.say("yay boobies!")
            engine.runAndWait()
        if eachPrediction == "butt":
            engine.say("BUTT FRENZY!")
            engine.runAndWait()
        print("detected", eachPrediction, " : ", eachProbability)
    time.sleep(5)


