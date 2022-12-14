from pico2d import *
import game_framework
import play_state
import stage_select_state

goal_image = None
up_y = None
forward = None
move_time = None
bgm = None
def enter():
    global goal_image,up_y, forward,move_time
    goal_image = load_image('resource\\goal\\GOAL_image.png')
    up_y=0
    forward = True
    move_time = 0

    global bgm
    bgm = load_wav('resource\\sound\\goal_sound.wav')
    bgm.set_volume(25)
    bgm.play(1)


def exit():
    global goal_image,up_y,forward
    goal_image = None
    up_y = None
    forward = None
    global bgm
    bgm = None


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    global forward, up_y,move_time
    if forward:
        up_y+=1
        if up_y > 30:
            forward = False
    else:
        up_y -= 1
        if up_y < -30:
            forward = True
    play_state.yoshi.x += 3
    move_time+=1
    if move_time>=164:
        play_state.on_quit_game()
        if stage_select_state.select_stage == stage_select_state.playable_stage:
            stage_select_state.playable_stage += 1
        if stage_select_state.playable_stage > 4: stage_select_state.playable_stage=4
        game_framework.pop_state()
        return
    if up_y%6 == 0 :
        play_state.yoshi.frame = (play_state.yoshi.frame+1)%8

    delay(0.01)


def draw():
    clear_canvas()
    play_state.draw_world()
    draw_goal()
    update_canvas()

def draw_goal():
    global up_y
    #G
    goal_image.clip_draw(
        14,
        250-42-192,
        148,
        192,
        get_canvas_width()//2-188-35,
        get_canvas_height()//2+100 - up_y
    )
    #O
    goal_image.clip_draw(
        168,
        250 - 15 - 192,
        152,
        192,
        get_canvas_width() // 2 - 30-35,
        get_canvas_height() // 2+100+up_y
    )
    #A
    goal_image.clip_draw(
        321,
        250 - 45 - 194,
        148,
        194,
        get_canvas_width() // 2 + 119-35,
        get_canvas_height() // 2+100-up_y
    )
    #L
    goal_image.clip_draw(
        475,
        250 - 14 - 194,
        142,
        194,
        get_canvas_width() // 2 + 267-35,
        get_canvas_height() // 2+100+up_y
    )
    #!
    goal_image.clip_draw(
        619,
        250 - 42 - 190,
        54,
        190,
        get_canvas_width() // 2 + 363-35,
        get_canvas_height() // 2+100-up_y
    )