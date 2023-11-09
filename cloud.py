from pico2d import load_image

import game_framework
import game_world

background_x, background_y = 800,549


class Cloud:
    image = None

    def __init__(self):
        if Cloud.image == None:
            Cloud.image == load_image('cloud.png')
        self.x, self.y,self.velocity = 200, 400, 1

        self.dir = 0
        self.image = load_image('cloud.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time
        if self.x > background_x:
            game_world.remove_object(self)
            #game_world.add_object()


