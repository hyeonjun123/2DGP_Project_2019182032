from pico2d import *
import game_framework
import logo_mode as start_mode

background_x, background_y = 800,549

open_canvas(background_x,background_y) #background 픽셀크기
game_framework.run(start_mode) #logo 모드로 시작 2초후 - > 타이틀 모드  클릭  후 -> 플레이 모드
close_canvas()
