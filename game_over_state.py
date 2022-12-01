from pico2d import *
import game_framework
import play_state
import stage_select_state

# goal_image = None
animation_image = None
animation_time = None
game_over_image= None
game_over_time = None
press_space_img = None

def enter():
    global animation_image
    animation_image=list()
    for i in range(1, 41):
        strr = 'resource\\yoshi_island_game_over\\yoshi_island_game_over ('+str(i)+').png'
        animation_image.append(load_image(strr))
    global animation_time
    animation_time = 0

    global game_over_image, game_over_time
    game_over_image = list()
    for i in range(53, 62):
        strr = 'resource\\yoshi_island_game_over\\yoshi_island_game_over (' + str(i) + ').png'
        game_over_image.append(load_image(strr))

    global press_space_img
    press_space_img=load_image('resource\\yoshi_island_game_over\\press_space_to_title.png')


def exit():
    pass
    # global goal_image,up_y,forward
    # goal_image = None
    # up_y = None
    # forward = None


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == 96:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            play_state.on_quit_game()
            game_framework.pop_state()
    pass


def update():
    global animation_time

    animation_time += 0.2
    if(animation_time >= 50):
        animation_time = 41
    print(animation_time)
    pass

def draw():
    clear_canvas()
    cw = get_canvas_width()
    ch = get_canvas_height()
    if animation_time<=40:
        iw = animation_image[int(animation_time)].w
        ih = animation_image[int(animation_time)].h

        animation_image[int(animation_time)].clip_draw(
            0,
            0,
            iw,
            ih,
            cw//2,
            ch//2,
            cw,
            ch
        )
    else:
        iw = game_over_image[int(animation_time) - 41].w
        ih = game_over_image[int(animation_time)-41].h
        game_over_image[int(animation_time)-41].clip_draw(
            0,
            0,
            iw,
            ih,
            cw // 2,
            ch // 2,
            cw,
            ch
        )
        press_space_img.draw(
            cw//4,
            ch//6
        )

    update_canvas()
    pass

