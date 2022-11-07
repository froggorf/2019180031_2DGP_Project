import game_framework
from pico2d import *
import yoshi_character
import stage
import pause_state
import start_state

X = 0
Y = 1
quit_game = False
gameMode = {"START":0, "SELECTSTAGE":1 ,"PLAYSTAGE":2}
yoshi =None
stageState = None

def enter():
    global X,Y
    X = 0
    Y = 1
    global pressA, pressD
    pressA = False
    pressD = False
    global gameMode, yoshi, stageState
    gameMode = {"START": 0, "SELECTSTAGE": 1, "PLAYSTAGE": 2}
    yoshi = yoshi_character.Yoshi()
    stageState = stage.StageState()
    global quit_game
    quit_game=False
    game_framework.push_state(start_state)

def exit():
    global X, Y
    del X
    del Y
    global pressA, pressD
    del pressA
    del pressD
    global gameMode, yoshi, stageState
    del gameMode
    del yoshi
    del stageState
    global quit_game
    del quit_game

def update():
    yoshi.update()
    stageState.update()

def draw_world():
    stageState.draw(yoshi.x, yoshi.y)
    yoshi.draw()


def draw():
    clear_canvas()
    stageState.draw(yoshi.x,yoshi.y)
    yoshi.draw()
    # for rect in stageState.groundRect:
    #     pico2d.draw_rectangle(rect.left,rect.bottom, rect.right,rect.top)
    update_canvas()
    delay(0.01)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == 96:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        handle_yoshi(event)

def on_quit_game():
    global quit_game
    quit_game=True

def resume():
    if quit_game == True:
        game_framework.pop_state()

def pause():
    pass

def handle_yoshi(event):
    yoshi.handle_event(event)

    if event.key == SDLK_F1:
        yoshi.y += 500