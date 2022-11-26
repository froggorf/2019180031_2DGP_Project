from pico2d import *


class UI:
    image = None
    def __init__(self):
        if UI.image == None:
            UI.image = load_image('ui.png')



class EggUi(UI):
    def __init__(self):
        super(EggUi, self).__init__()
        pass

    def draw(self, egg_count):
        UI.image.clip_draw(
            0,
            UI.image.h-182,
            200,
            100,
            get_canvas_width()-100,
            get_canvas_height()-50
        )

        UI.image.clip_draw(
            40*egg_count,
            UI.image.h - 80,
            40,
            81,
            get_canvas_width()-50,
            get_canvas_height()-50
        )