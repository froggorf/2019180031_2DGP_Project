import game_framework
from pico2d import *

import game_world
import yoshi_character
import stage
import pause_state
import stage_select_state
import start_state
import enemy
import ui

import stage1_status
import stage2_status

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
babyMario = None
tongue = None
eggs= None
eventbox =None

stageState = None
enemies = None
pressA= None
pressD = None

spawnMario = None
spawnTongue = None
spawnEgg = None

uilist = None
game_over_timer_ui = None
coin_ui = None
stage_bgm = None

def enter():
    global X,Y
    X = 0
    Y = 1
    global pressA, pressD
    pressA = False
    pressD = False

    global gameMode, yoshi, stageState, enemies,groundRect
    global stairRect, ceilingBlock,footBlock,largeBlock,jumpBlock,coins ,finishLine,babyMario
    global uilist,game_over_timer_ui,coin_ui
    game_over_timer_ui = ui.GameOverTimerUI()
    coin_ui= ui.CoinUI()

    uilist = [ui.EggUi()]
    global eggs,eventbox
    global stage_bgm
    eggs = []

    gameMode = {"START": 0, "SELECTSTAGE": 1, "PLAYSTAGE": 2}

    yoshi = yoshi_character.Yoshi()
    game_world.add_object(yoshi,1)

    if stage_select_state.select_stage == 1:
        stage1_status.input_object_to_game_world()
    elif stage_select_state.select_stage==2:
        stage2_status.input_object_to_game_world()


    stageState = stage.StageState()
    game_world.add_object(stageState,0)

    global quit_game
    quit_game=False
    game_framework.push_state(start_state)


def exit():
    global X, Y
    X = None
    Y = None
    global pressA, pressD
    pressA = None
    pressD = None
    global gameMode, yoshi, stageState, enemies,eventbox
    gameMode = None
    yoshi = None
    stageState = None
    enemies = None
    eventbox=None
    global quit_game
    quit_game = None
    global groundRect, stairRect,ceilingBlock, footBlock, largeBlock, jumpBlock, coins, finishLine
    groundRect = None
    stairRect = None
    ceilingBlock = None
    footBlock = None
    largeBlock = None
    jumpBlock = None
    coins = None
    finishLine = None
    global spawnMario, spawnTongue, spawnEgg,uilist,coin_ui,game_over_timer_ui
    spawnMario = None
    spawnTongue = None
    spawnEgg = None
    uilist = None
    coin_ui=None
    game_over_timer_ui=None
    game_world.clear()
    global stage_bgm
    stage_bgm.stop()
    stage_bgm = None

def update():
    global spawnMario, spawnTongue, spawnEgg
    for game_object in game_world.all_objects():
        game_object.update()
    # yoshi.update()
    # enemies.update()
    # stageState.update()

    if spawnMario:
        game_world.add_object(babyMario, 1)
        game_world.add_collision_group(yoshi, babyMario, 'yoshi:babyMario')
        game_world.add_collision_group(babyMario, groundRect, 'babyMario:groundRect')
        game_world.add_collision_group(babyMario, stairRect, 'babyMario:stairRect')
        game_world.add_collision_group(babyMario, ceilingBlock, 'babyMario:ceilingBlock')
        game_world.add_collision_group(babyMario, footBlock, 'babyMario:footBlock')
        game_world.add_collision_group(babyMario, largeBlock, 'babyMario:largeBlock')

        spawnMario = False
    if spawnTongue:
        game_world.add_object(tongue, 1)
        game_world.add_collision_group(tongue,enemies, 'tongue:enemies')
        spawnTongue = False
    if spawnEgg:
        game_world.add_objects(eggs,1)
        game_world.add_collision_group(eggs, enemies,'eggs:enemies')
        game_world.add_collision_group(eggs, groundRect, 'eggs:groundRect')
        game_world.add_collision_group(eggs, stairRect, 'eggs:stairRect')
        game_world.add_collision_group(eggs, ceilingBlock, 'eggs:ceilingBlock')
        game_world.add_collision_group(eggs, footBlock, 'eggs:footBlock')
        game_world.add_collision_group(eggs, largeBlock, 'eggs:largeBlock')
        game_world.add_collision_group(eggs, eventbox, 'eggs:eventbox')
        game_world.add_collision_group(eggs,coins,'eggs:coins')
        spawnEgg=False
    if yoshi.state == "NOMARIO":
        game_over_timer_ui.update()
    for a,b,group in game_world.all_collision_pairs():
        if collide(a,b):
            #print('Collision by', group)
            a.handle_collision(b,group)
            b.handle_collision(a, group)

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
    for uid in uilist:
        uid.draw(yoshi.egg_count)
    if yoshi.state == "NOMARIO":
        game_over_timer_ui.draw()
    coin_ui.draw()
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
    print(pressA, pressD)
    stage_bgm.resume()
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

    stage_bgm.pause()
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