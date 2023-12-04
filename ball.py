from pico2d import *
import game_world
import game_framework

ground_y = 100
sky_y = 500
ground_xl = 30
ground_xr = 770

net_xl = 350
net_xr = 450
net_yu = 250
net_yd = 50


background_x, background_y = 800, 549

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Ball:
    image = None

    def __init__(self, x=700, y=700, velocity=4):

        if Ball.image == None:
            Ball.image = load_image('ball.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.dir_y = -1
        self.dir_x = 0

    def draw(self):
        # draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 71, 0, 70, 70, self.x, self.y, 100, 100)  # ball_size 71 70

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time*self.velocity
        self.x += self.dir_x * RUN_SPEED_PPS * game_framework.frame_time*self.velocity

        if self.y < ground_y:
            self.dir_y = 1.3
            self.velocity = 3
        if self.y > sky_y:
            self.dir_y = -1.5
            self.dir_x = self.dir_x *1.4
            self.velocity = 3
        if self.x < ground_xl:
            self.dir_x = 1.3
            self.velocity = 4
        if self.x > ground_xr:
            self.dir_x = -1.2
            self.velocity = 4

        pass
        # self.x += self.velocity * 100 * game_framework.frame_time

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    # def handle_collision(self, group, other):
    #     if group == 'pikachu_left:ball':
    #         game_world.remove_object(self)
