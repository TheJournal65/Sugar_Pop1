import pygame as pg
import pymunk  # Import Pymunk library
import sys
from settings import *

class hud:
    def __init__(self) -> None:
        pass
    
    def draw_hud(self, total_sugar_count, grains, font, bucket_list, screen, level, gravity):
        """Draws the HUD\n
        total_sugar_count: sugar count variable\n
        grains: list of sugar grains\n
        font: font variable\n
        bucket_list: List of buckets\n
        screen: Screen Surface\n
        level: current level number\n
        gravity: the space.gravity of th world"""
        if total_sugar_count:
            if gravity[1] > 0:
                grav_text = 'UP'
            else:
                grav_text = 'DOWN'
            text_surface = font.render(f'Total Sugar: {total_sugar_count} Sugar Left: {total_sugar_count - len(grains)} Level {level} Gravity {grav_text}', True, (255, 255, 255))
            
            for bucket in bucket_list:
                bucket_surface = font.render(f"{bucket.needed_sugar - bucket.count}", True, (255,0,0))
                if not bucket.exploded: # Gets rid of the text if the bucket is exploded
                    # Draws how much sugar each bucket needs to the bucket's center position
                    screen.blit(bucket_surface, (bucket.get_pos()[0], bucket.get_pos()[1]))
                # Draw the text surface on the screen
                screen.blit(text_surface, (10, 10))  # Position at top-left corner
