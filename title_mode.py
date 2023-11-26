from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time
from sdl2 import SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE, SDLK_SPACE

import game_framework
import play_mode
import logo_mode


def init():
    global image
    image = load_image('title.png') #title png 업로드



def finish():
    global image
    del image

def handle_events():
    events = get_events()
    #event키 esc 누르면 종료
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)

def update():
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()