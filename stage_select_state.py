from pico2d import *
import game_framework
import play_state

select_stage_image = None
icon_image = None
icon_size = None
playable_stage = None
icon_pos = None
X,Y = None,None
select_stage = None
bgm = None
def enter():
    global select_stage_image, icon_image
    global icon_size
    global playable_stage
    global icon_pos
    global X,Y
    global select_stage
    select_stage_image = load_image('resource\\stage_select\\stage_select.png')
    icon_image = load_image('resource\\stage_select\\stage_icon.png')
    icon_size=[110,120]
    playable_stage = 4
    icon_pos = [[],[50,186],[240,186], [431,186],[625,186]]
    X,Y = 0,1
    select_stage = 0
    global bgm
    bgm = load_music('resource\\sound\\select_stage_sound.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()


def exit():
    global select_stage_image, icon_image, icon_size
    global playable_stage, icon_pos, X,Y, select_stage
    select_stage_image = None
    icon_image = None
    icon_size = None
    playable_stage = None
    icon_pos= None
    X= None
    Y= None
    select_stage= None
    global bgm
    bgm.stop()
    bgm = None




def pause():
    bgm.stop()
    pass


def resume():
    bgm.repeat_play()
    pass


def handle_events():
    global select_stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            #game_framework.push_state(play_state)
        elif event.type==SDL_KEYDOWN and event.key == SDLK_1:
            select_stage = 1
            game_framework.push_state(play_state)
        elif event.type==SDL_KEYDOWN and event.key == SDLK_2:
            if playable_stage<2:
                break
            else:
                select_stage =2
                game_framework.push_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            if playable_stage<3:
                break
            else:
                select_stage = 3
                game_framework.push_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            if playable_stage < 4:
                break
            else:
                select_stage = 4
                game_framework.push_state(play_state)


def update():
    pass


def draw():
    global icon_image
    global icon_size
    clear_canvas()
    select_stage_image.draw(get_canvas_width()//2,get_canvas_height()//2)
    for i in range(1,5):
        if playable_stage >= i:
            icon_image.clip_draw(icon_size[X]*(i-1),0,icon_size[X],icon_size[Y],icon_pos[i][X]+icon_size[X]//2,get_canvas_height()-(icon_pos[i][Y]+icon_size[Y]//2))


    update_canvas()
