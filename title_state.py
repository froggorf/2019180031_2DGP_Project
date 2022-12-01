from pico2d import *

import game_framework
#import play_state
import stage_select_state
image = None
image_time = 0
image_logo = None
loading = None
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
        strr = 'resource\\title_image\\frame_apngframe'+idx+'.png'
        image.append(load_image(strr))
    image_time = 0
    #image = load_image('title.png')

def exit():
    global image
    image = None

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


