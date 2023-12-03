from pico2d import *
import game_world
import game_framework

class background2:
    def __init__(self):
        self.image = load_image('background.png')

    #네트 충돌구현########
    def draw(self):
        self.image.draw(800//2, 549//2)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 399, 50, 399, 250
    ####################



    def update(self):
        pass
