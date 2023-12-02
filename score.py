from pico2d import load_image

import game_framework
import game_world
import random
import ball

background_x, background_y = 800,549

class Score:
    image = None

    def __init__(self, ball_instance):
        if Score.image == None:
            Score.image = load_image('score.png')
        self.x, self.y = 700, 500
        self.dir = 0
        self.score = 0
        self.ball_instance = ball_instance

    def draw(self):
        self.image.clip_draw(self.score * 34, 0, 34, 34, self.x, self.y)


    def update(self):
        if self.ball_instance.y < ball.ground_y and self.ball_instance.x < 400:
            self.score += 1
        pass



