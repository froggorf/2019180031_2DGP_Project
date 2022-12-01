from pico2d import *

import game_framework
import game_over_state
import play_state


class UI:
    image = None
    def __init__(self):
        if UI.image == None:
            UI.image = load_image('resource\\UI\\ui.png')


class CoinUI(UI):
    def __init__(self):
        super(CoinUI, self).__init__()
        pass

    def draw(self):
        #코인 출력
        UI.image.clip_draw(
            0,
            800-183-80,
            60,
            80,
            50,
            get_canvas_height()-50
        )
        #십의자리
        coin_num = play_state.stageState.coin_num

        if coin_num >= 10:
            UI.image.clip_draw(
                40*(coin_num//10),
                720,
                40,
                81,
                130,
                get_canvas_height()-50
            )
            # 일의자리
            UI.image.clip_draw(
                40 * (coin_num % 10),
                720,
                40,
                81,
                190,
                get_canvas_height() - 50
            )
        else:
            UI.image.clip_draw(
                40 * (coin_num % 10),
                720,
                40,
                81,
                150,
                get_canvas_height() - 50
            )




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
    bgm = None
    def __init__(self):
        super(GameOverTimerUI, self).__init__()
        self.time = 10
        self.counter = 0
        if GameOverTimerUI.bgm ==None:
            GameOverTimerUI.bgm = load_wav('resource\\sound\\game_over_timer.wav')
        self.bgm_time = 0

    def start_setting(self):
        self.time = 10
        self.counter = 0

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
        self.bgm_time+= (1/60)
        if self.bgm_time >=1.5 and self.time<=5:
            GameOverTimerUI.bgm.play(1)
            self.bgm_time=0
        self.counter+=16
        if self.counter>=1000:
            self.counter-=1000
            self.time-=1
            print(self.time)
            if self.time<0:
                self.time = 0
                game_framework.change_state(game_over_state)

        pass