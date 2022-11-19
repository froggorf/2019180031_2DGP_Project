from pico2d import *
import play_state
import game_framework

image = None
move = None
time = None
def enter():
    global image, move, time
    image = [load_image('stage1_start.png')]
    move = [0, 400]
    time = 0
    play_state.yoshi.x = -60
    play_state.yoshi.y = 700
    play_state.pressA= False
    play_state.pressD=False
def exit():
    global image, move, time
    del image
    del move
    del time

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.key == SDLK_a:
            if event.type == SDL_KEYDOWN:
                play_state.pressA  =True
            else:
                play_state.pressA  =False
        elif event.key == SDLK_d:
            if event.type == SDL_KEYDOWN:
                play_state.pressD = True
            else:
                play_state.pressD  =False

    pass

def update():
    global time
    if time <30:
        play_state.yoshi.x += 7
        play_state.yoshi.y -=2
        time += 1
    elif time<60:
        play_state.yoshi.x += 5
        play_state.yoshi.y -= 2
        time += 1
    elif time<80:
        play_state.yoshi.x += 4
        play_state.yoshi.y -= 3
        time += 1
    else:
        game_framework.pop_state()

    delay(0.01)
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image[0].draw(get_canvas_width()//2,get_canvas_height()//4*3)
    update_canvas()
