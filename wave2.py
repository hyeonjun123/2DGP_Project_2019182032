from pico2d import load_image

import game_framework
import game_world
import random

background_x, background_y = 800,549


class Wave:
    image = None

    def load_images(self):
        pass

    def __init__(self):
        if Wave.image == None:
            Wave.image == load_image('wave.png')
        self.x, self.y,self.velocity = random.randint(0,800),random.randint(0,5), 0.3
        self.dir = 0
        self.image = load_image('wave.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.velocity * 100 * game_framework.frame_time
        if self.y > 15:
            self.velocity = -0.3
        if self. y <-100:
            self.velocity = 0.3



