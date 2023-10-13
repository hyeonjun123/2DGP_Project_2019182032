from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 805

idle_1, idle_2 = True, True #정지모션

dir_x, dir_x2 = 0, 0
dir_y, dir_y2 = 0, 0

x,x2 = 170, 680
y,y2 = 197.5, 197.5


def load_resources():
    global volleyball_ground, volleyball_net, arrow, king_icon
    global character, character2

    arrow = load_image('hand_arrow.png')
    volleyball_ground = load_image('Evening_background3.png')
    volleyball_net = load_image('volleyball_net_1.png')


    character = load_image('animation_sheet4.png') #사람
    character2 = load_image('animation_sheet4.png') #마법사#


def handle_events():
    global running #화면 실행
    global dir_x, dir_y, dir_x2, dir_y2 #캐릭터 x,y좌표
    global mx, my  #마우스 x,y좌표
    global idle_1, idle_2 #캐릭터2의 정지

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
             running = False
        elif event.type == SDL_KEYDOWN:

            # character1의 이동
            if event.key == SDLK_d:
                dir_x += 1

                idle_1 = False
            elif event.key == SDLK_a:
                dir_x -= 1
                idle_1 = False
            elif event.key == SDLK_w:
                dir_y += 1
                idle_1 = False
            elif event.key == SDLK_s:
                dir_y -= 1
                idle_1 = False


            # character2의 이동
            if event.key == SDLK_RIGHT:
                dir_x2 += 1
                idle_2 = False
            elif event.key ==SDLK_LEFT:
                dir_x2 -= 1
                idle_2 = False
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dir_y2 +=1
                idle_2 = False
            elif event.key == SDLK_DOWN:
                dir_y2 -=1
                idle_2 = False


        elif event.type == SDL_KEYUP:
        #idle이 true이면 idle 모션을 넣어준다.
            if event.key == SDLK_d:
                dir_x -= 1
                idle_1 = True
            elif event.key == SDLK_a:
                dir_x += 1
                idle_1 = True
            if event.key == SDLK_w:
                dir_y -= 1
                idle_1 = True
            elif event.key == SDLK_s:
                dir_y += 1
                idle_1 = True

            if event.key == SDLK_RIGHT:
                dir_x2 -= 1
                idle_2 = True
            elif event.key == SDLK_LEFT:
                dir_x2 += 1
                idle_2 = True
            if event.key == SDLK_UP:
                dir_y2 -= 1
                idle_2 = True
            elif event.key == SDLK_DOWN:
                dir_y2 += 1
                idle_2 = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



def set_character_direction(dx):
    # 캐릭터의 이동 방향을 설정하는 함수
    global character_scale_x

    if dx > 0:
        character_scale_x = 1  # 오른쪽으로 이동하면 원래 방향대로
    else:
        character_scale_x = -1  # 왼쪽으로 이동하면 이미지를 뒤집음





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
    volleyball_ground.draw(TUK_WIDTH //2, TUK_HEIGHT//2)
    volleyball_net.draw(412, 225)

    #king_icon.draw(512,512)

#character1 render
    if idle_1 == True:
        character.clip_draw(0, 0, 120, 130, x, y)
        print(x,y)
    elif idle_1==False:
        character.clip_draw(frame * 120, 0, 120, 130, x, y)



#character2 render
    if idle_2 == True:
        character2.clip_draw(0, 260, 120, 130, x2, y2)
    elif idle_2==False:
            character2.clip_draw(frame * 120, 260, 120, 130, x2, y2)
    update_canvas()




def update_world():
    global frame
    global t, action
    global x, y, x2, y2 #화면상에 그려질 위치
    frame = (frame + 1) % 8

    x += dir_x * 5
    y += dir_y * 5

    #화면 밖으로 나가지 못하게
    if (80 <= x2 <= 1200 and 100 <= y2 <= 970):
        x2 += dir_x2 * 5
        y2 += dir_y2 * 5

    else:
        if(x2<80):
            x2 = 80 + 10
        elif(x2 > 1200):
            x2 = 1200 - 10 # 오른 벽

        if(y2 <100):
            y2 = 100 + 10 #밑
        elif(y2 > 970):
            y2 = 970 - 10 #위

    delay(0.01)




open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()


while running:
    handle_events()  # 사용자 입력을 받아들인다.
    render_world()  # 월드의 현재 내용을 그린다.
    update_world()  # 월드안의 객체들의 상호작용을 계산하고, 그 결과를 update한다.

close_canvas()
