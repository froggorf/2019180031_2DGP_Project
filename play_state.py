import game_framework
from pico2d import *

import game_world
import yoshi_character
import stage
import pause_state
import start_state
import enemy

import stage1_status
X = 0
Y = 1
quit_game = False
gameMode = {"START":0, "SELECTSTAGE":1 ,"PLAYSTAGE":2}
yoshi =None
groundRect = None
stairRect = None
ceilingBlock = None
footBlock = None
largeBlock = None
jumpBlock = None
coins = None
finishLine = None

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

    global gameMode, yoshi, stageState, enemies,groundRect
    global stairRect, ceilingBlock,footBlock,largeBlock,jumpBlock,coins ,finishLine
    gameMode = {"START": 0, "SELECTSTAGE": 1, "PLAYSTAGE": 2}

    yoshi = yoshi_character.Yoshi()
    game_world.add_object(yoshi,1)

    enemies = [enemy.Flower(800,700)]
    game_world.add_objects(enemies, 1)

    stage1_status.input_object_to_game_world()

    stageState = stage.StageState()
    game_world.add_object(stageState,0)

    global quit_game
    quit_game=False
    #TODO: 나중에 다시 키기
    game_framework.push_state(start_state)

    #충돌체크 그룹 추가
    game_world.add_collision_group(yoshi, groundRect, 'yoshi:groundRect')
    game_world.add_collision_group(yoshi, stairRect, 'yoshi:stairRect')
    game_world.add_collision_group(yoshi, ceilingBlock, 'yoshi:ceilingBlock')
    game_world.add_collision_group(yoshi, footBlock, 'yoshi:footBlock')
    game_world.add_collision_group(yoshi, largeBlock, 'yoshi:largeBlock')
    game_world.add_collision_group(yoshi, jumpBlock, 'yoshi:jumpBlock')
    game_world.add_collision_group(yoshi, coins, 'yoshi:coins')
    game_world.add_collision_group(yoshi, finishLine, 'yoshi:finishLine')
    game_world.add_collision_group(yoshi, enemies, 'yoshi:enemies')


    game_world.add_collision_group(enemies, groundRect, 'enemies:groundRect')
    game_world.add_collision_group(enemies, stairRect, 'enemies:stairRect')
    game_world.add_collision_group(enemies, ceilingBlock, 'enemies:ceilingBlock')
    game_world.add_collision_group(enemies, footBlock, 'enemies:footBlock')
    game_world.add_collision_group(enemies, largeBlock, 'enemies:largeBlock')
    game_world.add_collision_group(enemies, jumpBlock, 'enemies:jumpBlock')

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
    global groundRect, stairRect,ceilingBlock, footBlock, largeBlock, jumpBlock, coins, finishLine
    del groundRect,stairRect,ceilingBlock,footBlock,largeBlock,jumpBlock,coins,finishLine
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # yoshi.update()
    # enemies.update()
    # stageState.update()

    for a,b,group in game_world.all_collision_pairs():
        if collide(a,b):
            #print('Collision by', group)
            a.handle_collision(b,group)
            a.handle_collision(a, group)

def draw_world():
    #TODO: 인자 다 import로 해버리기
    for game_object in game_world.all_objects():
        game_object.draw(*stageState.get_camera())
    # stageState.draw(yoshi.x, yoshi.y)
    # yoshi.draw()
    # enemies.draw(*stageState.get_camera())


def draw():
    clear_canvas()
    draw_world()
    # stageState.draw(yoshi.x,yoshi.y)
    # yoshi.draw()
    # enemies.draw(*stageState.get_camera())

    update_canvas()
    # delay(0.01)

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


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True