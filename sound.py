import pygame as pg
import pymunk  # Import Pymunk library
import sys
from settings import *

class Sound:
    def __init__(self) -> None:
        pg.mixer.init()
    
    def vine_booom():
        boom_boom = pg.mixer.Sound("audio\explosion-sound-effect-2-241820.mp3")
        boom_boom.set_volume(.2)
        pg.mixer.Sound.play(boom_boom)
        
    def sugar_thang():
        sugar_drop = pg.mixer.Sound("audio\happy-pop-2-185287.mp3")
        sugar_drop.set_volume(.01)
        pg.mixer.Sound.play(sugar_drop)
    
    def level_win():
        ya_hoo = pg.mixer.Sound("audio\level-win-6416.mp3")
        ya_hoo.set_volume(.5)
        pg.mixer.Sound.play(ya_hoo)