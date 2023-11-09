from pico2d import load_image

import game_framework


class Cloud:
    def __init__(self):
        self.x, self.y = 200, 400
        self.velocity = 1
        self.dir = 0
        self.image = load_image('cloud.png')

    def draw(self):
        self.x += self.velocity * 100 * game_framework.frame_time
        self.image.draw(self.x, self.y)


    def update(self):
        pass

