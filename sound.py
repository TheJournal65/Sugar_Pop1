import pygame as pg
import pymunk  # Import Pymunk library
import sys
from settings import *

class Sound:
    def __init__(self) -> None:
        pg.mixer.init()
        self.sound_list = []
        for i in SOUNDS:
            self.sound_list.append((i, pg.mixer.Sound(SOUNDS[i][0]), pg.mixer.Channel(SOUNDS[i][1])))
            SOUND_LIST.extend(self.sound_list)
    
    def play(name):
        """Pass the name of the sound to play"""
        for i in SOUND_LIST:
            if name == i[0]:
                i[2].play(i[1])
                