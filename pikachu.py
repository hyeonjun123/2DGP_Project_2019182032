# 이것은 각 상태들을 객체로 구현한 것임.
from pico2d import *
from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT

import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

ground_y = 130
jump_y = 250

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT
def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT
def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT
def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT
def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE
def time_out(e):
    return e[0] == 'TIME_OUT'
def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP
def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP



class Idle:

    @staticmethod
    def enter(pikachu, e):
        if pikachu.face_dir == -1:
            pikachu.action = 2
        elif pikachu.face_dir == 1:
            pikachu.action = 3
        pikachu.dir = 0
        pikachu.frame = 0
        pikachu.wait_time = get_time()  # pico2d import 필요
        pass

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.fire_ball()
        pass

    @staticmethod
    def do(pikachu):
        if get_time() - pikachu.wait_time > 2:
            # pikachu.state_machine.handle_event(('TIME_OUT', 0))
            pass

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.image.clip_draw(0, 65, 68, 65, pikachu.x, pikachu.y, 150, 150)

        elif pikachu.face_dir == -1:
            pikachu.image.clip_composite_draw(0, 65, 68, 65, 0, 'h', pikachu.x, pikachu.y, 150, 150)


class Run:

    @staticmethod
    def enter(pikachu, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pikachu.dir, pikachu.action, pikachu.face_dir = 1, 1, 1
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pikachu.dir, pikachu.action, pikachu.face_dir = -1, 0, -1

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.fire_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        pikachu.x += pikachu.dir * RUN_SPEED_PPS * game_framework.frame_time
        pass

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.image.clip_draw(int(pikachu.frame) * 66, 65 * 3, 68, 65, pikachu.x, pikachu.y, 150, 150)

        elif pikachu.face_dir == -1:
            pikachu.image.clip_composite_draw(int(pikachu.frame) * 66, 65 * 3, 68, 65, 0, 'h', pikachu.x, pikachu.y, 150,
                                              150)

        # pikachu.image.clip_draw(pikachu.frame * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        # pikachu.image.clip_draw(pikachu.frame * 68, pikachu.action * 65, 68, 65, pikachu.x, pikachu.y)


class Jump:
    @staticmethod
    def enter(pikachu, e):
        if up_down(e):
            if pikachu.y < jump_y:  # jump높이까지 y높이를 높인다.
                pikachu.dir_y = 1

    @staticmethod
    def exit(pikachu, e):
        if space_down(e):
            pikachu.fire_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + 1) % 5

        if pikachu.y >= jump_y:
            pikachu.dir_y = -1 #pikachu.dir_y를 -1로 해준다.


        pikachu.y += pikachu.dir_y * RUN_SPEED_PPS * game_framework.frame_time

        if pikachu.y <= ground_y:
            pikachu.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == 1:
            pikachu.image.clip_draw(int(pikachu.frame) *66 ,  65*3, 68, 65, pikachu.x, pikachu.y, 150, 150)

        elif pikachu.face_dir == -1:
            pikachu.image.clip_composite_draw(int(pikachu.frame) *66,  65*3, 68, 65, 0, 'h', pikachu.x, pikachu.y, 150, 150)


class Sleep:

    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pass

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + 1) % 8

    @staticmethod
    def draw(pikachu):
        if pikachu.face_dir == -1:
            pikachu.image.clip_composite_draw(pikachu.frame * 100, 200, 100, 100,
                                              -3.141592 / 2, '', pikachu.x + 25, pikachu.y - 25, 100, 100)
        else:
            pikachu.image.clip_composite_draw(pikachu.frame * 100, 300, 100, 100,
                                              3.141592 / 2, '', pikachu.x - 25, pikachu.y - 25, 100, 100)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle, up_down : Jump},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run, up_down : Jump},
            Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run, up_down:Jump},
            Jump: {time_out:Idle}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Pikachu:
    def __init__(self):
        self.x, self.y = 400, 130
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.dir_y = 1
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = None

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):

        self.state_machine.draw()
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x -60, self.y -60, self.x+60, self.y+60


