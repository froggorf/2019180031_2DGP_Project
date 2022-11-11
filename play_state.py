import game_framework
from pico2d import *
import yoshi_character
import stage
import pause_state
import start_state
import enemy

X = 0
Y = 1
quit_game = False
gameMode = {"START":0, "SELECTSTAGE":1 ,"PLAYSTAGE":2}
yoshi =None
stageState = None
enemies = None
pressA= None
pressD = None

def enter():
    global X,Y
    X = 0
    Y = 1
    global pressA, pressD
    pressA = False
    pressD = False

    global gameMode, yoshi, stageState, enemies
    gameMode = {"START": 0, "SELECTSTAGE": 1, "PLAYSTAGE": 2}
    yoshi = yoshi_character.Yoshi()
    enemies = enemy.Flower(800,700)
    stageState = stage.StageState()
    global quit_game
    quit_game=False
    #TODO: 나중에 다시 키기
    game_framework.push_state(start_state)

def exit():
    global X, Y
    del X
    del Y
    global pressA, pressD
    del pressA
    del pressD
    global gameMode, yoshi, stageState, enemies
    del gameMode
    del yoshi
    del stageState
    del enemies
    global quit_game
    del quit_game

def update():
    yoshi.update()
    enemies.update()
    stageState.update()

def draw_world():
    stageState.draw(yoshi.x, yoshi.y)
    yoshi.draw()
    enemies.draw(*stageState.get_camera())


def draw():
    clear_canvas()
    stageState.draw(yoshi.x,yoshi.y)
    yoshi.draw()
    enemies.draw(*stageState.get_camera())

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
    if pressA and not pressD:
        yoshi.cur_state.exit(yoshi)
        yoshi.cur_state = yoshi_character.WALK
        yoshi.dir[X] -= 1
        yoshi.face = 0
    elif pressD and not pressA:
        yoshi.cur_state.exit(yoshi)
        yoshi.cur_state = yoshi_character.WALK
        yoshi.dir[X] += 1
        yoshi.face = 1

    if quit_game == True:
        game_framework.pop_state()



def pause():
    pass

def handle_yoshi(event):
    yoshi.handle_event(event)

    if event.key == SDLK_F1:
        yoshi.y += 500
    if event.key == SDLK_F2 and event.type == SDL_KEYDOWN:
        yoshi.x += 500