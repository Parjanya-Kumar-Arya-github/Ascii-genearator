import time

from PIL import Image
import cv2  # pip install opencv2
import os
from pygame import mixer  # pip install pygame
import sys
import threading

mixer.init()  # Initialzing pyamge mixer

mixer.music.load('Song.mp3')  # Add your own song here
if not (os.path.isdir('Frame')):
    vidObj = cv2.VideoCapture("blackdance.mp4")  # Add your own video here.
    count = 0
    success = 1

    os.makedirs('Frame')
    while success:
        try:
            success, image = vidObj.read()
            cv2.imwrite("Frame/frame%d.jpg" % count, image)
            count += 1
        except:
            break


musicplay = threading.Thread(target=mixer.music.play())


def player():
    run = True
    i = 0
    while run:
        try:
            img = Image.open(f"Frame/frame{i}.jpg")
            img = img.convert('L')
            ascii_string = " .:-=$*#%@"
            img = img.resize((100, 50))
            pixels = list(img.getdata())
            w, h = img.size
            Ascii_art = ""
            for pixel in range(len(pixels)):
                if pixel % w == 0:
                    Ascii_art = Ascii_art + "\n"
                Ascii_art = Ascii_art + ascii_string[pixels[pixel] // 50]

            print(Ascii_art)

            i += 1
            time.sleep(0.05)
            os.system('cls')
        except Exception as e:
            run = False
            sys.exit()


player()
