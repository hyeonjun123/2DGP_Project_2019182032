from pico2d import *
import game_world
import game_framework


background_x, background_y = 800,549


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):

        if Ball.image == None:
            Ball.image = load_image('ball.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame*71,0, 70, 70, self.x, self.y,100,100) #ball_size 71 70
        draw_rectangle(*self.get_bb())


    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time
        self.frame = (self.frame + 1) % 5
        delay(0.05)



    def get_bb(self):
        return self.x -40, self.y -40, self.x+40, self.y+40


    # def handle_collision(self, group, other):
    #     if group == 'boy:ball':
    #         game_world.remove_object(self)
    #     elif group == 'zombie:ball':
    #         game_world.remove_object(self)
