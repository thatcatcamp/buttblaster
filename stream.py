import datetime
import os
import shutil
import signal
import time
from os.path import join
from playsound import playsound

import pyttsx3
import cv2
from imageai.Classification.Custom import CustomImageClassification
from loguru import logger
from string import Template
import random
last_output = time.time()
execution_path = os.getcwd()
RAMDISK = "/tmp/swap.jpg"
TEST_MODE = True
BORED_TIMEOUT = 360
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


def update_view(boobs=False, butts=False, cats=True):
    replacements = dict(boobs=boobs, butts=butts, debug=TEST_MODE, gmt=datetime.datetime.utcnow().isoformat(), cats=cats)
    with open("template.html", "rt") as fh:
        data = fh.read()
        with open("/tmp/index.html", "w+t") as oh:
            oh.write(Template(data).safe_substitute(replacements))


def random_image():
    if random.randint(0,99) > 75:
        swap = random.choice(os.listdir("./test"))
        if swap is None:
            print("no test data?")
            return
        print("Adding random image...")
        shutil.copyfile(join("./test", swap), RAMDISK)


def random_sound(image_type: str):
    global last_output
    last_output = time.time()
    swap = random.choice(os.listdir(f"./wav/{image_type}"))
    if swap is None:
        print("no test data?")
        return
    print("playing...", swap)
    playsound(join(f"./wav/{image_type}", swap), RAMDISK)



logger.info("init")
signal.signal(signal.SIGINT, signal_handler)
camera = cv2.VideoCapture(1)
if not camera.isOpened():
    print("Cannot open camera")
    exit()
update_view()

# CAP_PROP_FPS doesn't work for this - use sleep
while True:
    ret, frame = camera.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imwrite(RAMDISK, frame)
    # add random images for testing
    if TEST_MODE:
        random_image()
    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, RAMDISK), result_count=1)

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        if eachPrediction == "boobs" and eachProbability > 50:
            update_view(boobs=True)
            random_sound("boobs")
        if eachPrediction == "butt" and eachProbability > 50:
            update_view(boobs=True)
            random_sound("butts")
        if eachPrediction == "cats" and eachProbability > 50:
            update_view(cats=True)
            random_sound("cats")
        print("detected", eachPrediction, " : ", eachProbability)
    if last_output+BORED_TIMEOUT < time.time():
        random_sound("bored")
    time.sleep(5)


