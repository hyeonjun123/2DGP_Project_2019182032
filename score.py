from pico2d import load_image

import game_framework
import game_world
import random

background_x, background_y = 800,549


class Score:
    image = None

    def load_images(self):
        pass

    def __init__(self):
        if Score.image == None:
            Score.image == load_image('score.png')
        self.x, self.y = 600,400
        self.dir = 0
        self.image = load_image('score.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass




