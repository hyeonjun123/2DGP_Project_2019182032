from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
idle_2 = True #정지모션
dir_x = 0
dir_y = 0
x = TUK_WIDTH / 2
y = TUK_HEIGHT / 2

def load_resources():
    global volleyball_ground, arrow, king_icon
    global character, character2


    arrow = load_image('hand_arrow.png')
    volleyball_ground = load_image('TUK_GROUND.png')
    #king_icon = load_image('king_icon.png')
    character = load_image('animation_sheet.png') #사람
    character2 = load_image('animation_sheet4.png') #마법사


def handle_events():
    global running #화면 실행
    global dir_x, dir_y #캐릭터 x,y좌표
    global mx, my  #마우스 x,y좌표
    global idle_2 #캐릭터2의 정지

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             running = False
        elif event.type == SDL_KEYDOWN:
            idle_2 = False
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key ==SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dir_y +=1
            elif event.key == SDLK_DOWN:
                dir_y -=1

        elif event.type == SDL_KEYUP:
            idle_2 = True
        #idle이 true이면 idle 모션을 넣어준다.
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
         # 마우스 이벤트
        # elif event.type ==SDL_MOUSEMOTION:
        #     mx,my = event.x, TUK_HEIGHT-1 -event.y
        #
        # elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
        #     points.append((event.x, TUK_HEIGHT-1-event.y))




def reset_world():
    global running, cx, cy, frame
    global t, action
    global mx,my

    mx,my = 0,0
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3




def render_world():

    clear_canvas()
    volleyball_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #king_icon.draw(512,512)

    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)


    if(idle_2 == True):
        character2.clip_draw(0,260,120,130,x,y)
    elif(idle_2==False):
        character2.clip_draw(frame * 120, 260, 120, 130, x, y)
    update_canvas()


def update_world():
    global frame
    global t, action
    global x, y
    frame = (frame + 1) % 8


#화면 밖으로 나가지 못하게
    if (80 <= x <= 1200 and 100 <= y <= 970):
        x += dir_x * 5
        y += dir_y * 5
    else:
        if(x<80):
            x= 80 +10
        elif(x >1200):
            x =1200-10 # 오른 벽

        if(y <100):
            y = 100+10 #밑
        elif(y >970):
            y = 970-10 #위
    delay(0.05)


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()


while running:
    handle_events()  # 사용자 입력을 받아들인다.
    render_world()  # 월드의 현재 내용을 그린다.
    update_world()  # 월드안의 객체들의 상호작용을 계산하고, 그 결과를 update한다.

close_canvas()
