

from pygame import mixer
from datetime import datetime
from time import time

# print("Press 'p' for pause, 'r' for resume, 's' for stop :")
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        # if a == "p":
        #     mixer.music.pause()
        # elif a == "r":
        #     mixer.music.unpause()
        # elif a == "s":
        #     mixer.music.stop()
        #     break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop("Jamie Duffy - Solas (Official Video).mp3")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyesecs = 10
    exsecs = 15
    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop alarm.")
            musiconloop('solas.mp3', 'drank')
            init_water = time()
            log_now("Drank water at")
        if time() - init_eyes > eyesecs:
            print("Eyes Exercise time. Enter 'doneeyes' to stop alarm.")
            musiconloop('solas.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes exercise done at")
        if time() - init_exercise > exsecs:
            print("Physical Exercise time. Enter 'donephy' to stop alarm.")
            musiconloop('solas.mp3', 'donephy')
            init_exercise = time()
            log_now("Exercise done at")
