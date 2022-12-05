from pico2d import *

import game_framework
#import play_state
import stage_select_state
image = None
image_time = 0
image_logo = None
loading = None
press_img = None
bgm = None
def enter():
    # fill here
    hide_cursor()
    hide_lattice()
    global image_logo,loading
    image_logo= load_image('resource\\title_image\\tukorea_logo.png')
    loading = False
    clear_canvas()
    image_logo.clip_draw(0, 0, image_logo.w, image_logo.h, get_canvas_width()//2, get_canvas_height()//2,get_canvas_width(),get_canvas_height())
    update_canvas()
    global press_img
    press_img = load_image('resource\\yoshi_island_game_over\\press_space_to_title.png')

    bggm = load_wav('resource\\sound\\yoshiiiii.wav')
    bggm.play(1)

    global image,image_time
    image = list()
    for i in range(1,148):
        idx = None
        if i//10 >= 10:
            idx = str(i)
        elif i//10>=1:
            idx = '0'+str(i)
        else:
            idx = '00'+str(i)
        image.append(load_image('resource\\title_image\\frame_apngframe'+idx+'.png'))
    image_time = 0
    global bgm
    bgm = load_music('resource\\sound\\title_sound.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()

    #image = load_image('title.png')

def exit():
    global image
    global bgm
    bgm.stop()
    bgm = None
    image = None
    global image_time,image_logo,loading
    image_time=None
    image_logo=None
    loading = None
    global press_img
    press_img=None

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(stage_select_state)


def draw():
    clear_canvas()


    image[int(image_time)].draw(
        get_canvas_width()//2,
        get_canvas_height()//2
    )
    press_img.draw(
        get_canvas_width() // 4,
        get_canvas_height() // 6
    )
    update_canvas()

def update():
    global image_time,loading

    image_time+=0.2
    if(image_time>=147):
        image_time = 0
    pass

def pause():
    pass

def resume():
    pass


