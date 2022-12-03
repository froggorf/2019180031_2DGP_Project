from pico2d import *
import play_state
import game_framework
import stage_select_state
import yoshi_character
image = None
move = None
time = None
bgm = None
def enter():
    global image, move, time
    image = [load_image('resource\\about_stage\\stage1_start.png')]
    move = [0, 400]
    time = 0

    play_state.yoshi.x = -60
    play_state.yoshi.y = 700
    if stage_select_state.select_stage==4:
        play_state.yoshi.x = 234
        play_state.yoshi.y = 217
        play_state.yoshi.cur_state=yoshi_character.IDLE_01
    play_state.pressA= False
    play_state.pressD=False
    global bgm
    bgm = load_music('resource\\sound\\start_sound.mp3')
    bgm.set_volume(32)
    bgm.play(1)
def exit():
    global image, move, time
    del image
    del move
    del time
    global bgm
    bgm.stop()
    del bgm

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
        if stage_select_state.select_stage != 4:
            play_state.yoshi.x += 7
            play_state.yoshi.y -=2
        time += 1
    elif time<60:
        if stage_select_state.select_stage != 4:
            play_state.yoshi.x += 5
            play_state.yoshi.y -= 2
        time += 1
    elif time<110:
        if stage_select_state.select_stage != 4:
            play_state.yoshi.x += 2
            play_state.yoshi.y -= 1
        time += 1
    else:
        game_framework.pop_state()
        if stage_select_state.select_stage == 1:
            play_state.stage_bgm = load_music('resource\\sound\\stage1_sound.mp3')
            play_state.stage_bgm.set_volume(32)
            play_state.stage_bgm.repeat_play()
        elif stage_select_state.select_stage == 2:
            play_state.stage_bgm = load_music('resource\\sound\\stage2_sound.mp3')
            play_state.stage_bgm.set_volume(32)
            play_state.stage_bgm.repeat_play()
        elif stage_select_state.select_stage == 3:
            play_state.stage_bgm = load_music('resource\\sound\\stage3_sound.mp3')
            play_state.stage_bgm.set_volume(32)
            play_state.stage_bgm.repeat_play()
        elif stage_select_state.select_stage == 4:
            play_state.stage_bgm = load_music('resource\\sound\\stage4_sound.mp3')
            play_state.stage_bgm.set_volume(32)
            play_state.stage_bgm.repeat_play()

    delay(0.01)
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image[0].draw(get_canvas_width()//2,get_canvas_height()//4*3)
    update_canvas()
