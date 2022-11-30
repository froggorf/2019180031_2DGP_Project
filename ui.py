from pico2d import *

import game_framework
import game_over_state

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

class GameOverTimerUI(UI):
    def __init__(self):
        super(GameOverTimerUI, self).__init__()
        self.time = 10
        self.counter = 0
    def start_setting(self):
        self.time = 10
        self.counter = 0
        print('초기화 됐는데?')

    def draw(self):
        #검은원
        UI.image.clip_draw(
            236,
            UI.image.h-81-164,
            164,
            164,
            get_canvas_width() - 164//2,
            get_canvas_height() - 100-164//2
        )

        #십의자리
        if self.time >= 10:
            UI.image.clip_draw(
                40 * int(self.time//10),
                UI.image.h - 80,
                40,
                81,
                get_canvas_width() - 164//2-30,
                get_canvas_height() - 100-164//2
            )

        #일의자리

        UI.image.clip_draw(
            40 * int(self.time % 10),
            UI.image.h - 80,
            40,
            81,
            get_canvas_width() - 164//2+30,
            get_canvas_height() - 100 - 164 // 2
        )
    def update(self):
        self.counter+=16
        if self.counter>=1000:
            self.counter-=1000
            self.time-=1
            print(self.time)
            if self.time<0:
                self.time = 0
                print("game_over_state 로 가기")
                game_framework.change_state(game_over_state)

        pass