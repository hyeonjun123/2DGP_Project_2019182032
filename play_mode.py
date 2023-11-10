from pico2d import *
import game_framework

import ball
import cloud
import game_world
from background import background2
import background
from pikachu import Pikachu

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            pikachu.handle_event(event)

def init():
    global background2
    global cloud
    global ball
    global pikachu

    running = True

    background2 = background2()
    game_world.add_object(background2, 0)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)


    #cloud추가
    for i in range(10):
        cloud_instance = cloud.Cloud()
        game_world.add_object(cloud_instance, 1)


    #ball추가
    ball = ball.Ball()
    game_world.add_object(ball, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()



def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
