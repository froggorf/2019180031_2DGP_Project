from pico2d import *
import random

yoshi_state = {"MARIO": 0 , "NOMARIO":1, "MARIO_SWALLOW":2, "NOMARIO_SWALLOW":3}
X = 0
Y = 1
LEFT = 0
RIGHT = 1
GRAVITY = 5
MAXJUMPTIME = 10
jump_delay = 0

#이벤트 정의
WD,WU,AD,AU,SD,SU,DD,DU,SHIFTD,SHIFTU = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): WD,
    (SDL_KEYUP, SDLK_w): WU,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYUP, SDLK_a): AU,
    (SDL_KEYDOWN, SDLK_s): SD,
    (SDL_KEYUP, SDLK_s): SU,
    (SDL_KEYDOWN, SDLK_d): DD,
    (SDL_KEYUP, SDLK_d): DU,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFTD,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFTU,
}

class IDLE_01:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):
        pass

    def draw(self):
        if self.face == RIGHT: #RIGHT
            self.image[yoshi_state[self.state]].clip_draw(
                int(62*1.6) * self.frame,
                0,
                int(62*1.6),
                int(66*1.6),
                self.camera[X] + int(62*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(62*1.6) * self.frame,
                160,
                int(62 * 1.6),
                int(66 * 1.6),
                self.camera[X] + int(62*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )

class IDLE_02:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):
        pass

    def draw(self):
        if self.face == RIGHT: #RIGHT
            self.image[yoshi_state[self.state]].clip_draw(
                int(62*1.6) * self.frame,
                320,
                int(62*1.6),
                int(66*1.6),
                self.camera[X] + int(62*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(62*1.6) * self.frame,
                480,
                int(62 * 1.6),
                int(66 * 1.6),
                self.camera[X] + int(62*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )

class WALK:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0

        pass

    def exit(self, event=None):
        pass

    def do(self):

        pass

    def draw(self):
        if self.face == RIGHT:
            self.image[yoshi_state[self.state]].clip_draw(
                int(64*1.6) * self.frame,
                640,
                int(64*1.6),
                int(66*1.6),
                self.camera[X] + int(64*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(64*1.6)*self.frame,
                800,
                int(64*1.6),
                int(66*1.6),
                self.camera[X] + int(64*1.6) // 2,
                self.camera[Y] + int(66*1.6) // 2
            )

class RUN:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):

        pass

    def draw(self):
        if self.face == RIGHT:
            self.image[yoshi_state[self.state]].clip_draw(
                int(72*1.6) * self.frame,
                960,
                int(72*1.6),
                int(68*1.6),
                self.camera[X] + int(72*1.6) // 2,
                self.camera[Y] + int(68*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(72*1.6) * self.frame,
                1120,
                int(72*1.6),
                int(68*1.6),
                self.camera[X] + int(72*1.6) // 2,
                self.camera[Y] + int(68*1.6)// 2
            )

class JUMP:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0

        pass

    def exit(self, event=None):

        pass

    def do(self):
        pass

    def draw(self):
        if self.face == RIGHT:
            self.image[yoshi_state[self.state]].clip_draw(
                0,
                1600,
                int(60*1.6),
                int(72*1.6),
                self.camera[X] + int(60*1.6) // 2,
                self.camera[Y] + int(72*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                0,
                1760,
                int(60 * 1.6),
                int(72 * 1.6),
                self.camera[X] + int(60 * 1.6) // 2,
                self.camera[Y] + int(72 * 1.6) // 2
            )

class FALL:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):
        pass

    def draw(self):
        if self.face == RIGHT:
            self.image[yoshi_state[self.state]].clip_draw(
                0,
                1920,
                int(58*1.6),
                int(62*1.6),
                self.camera[X] + int(58*1.6) // 2,
                self.camera[Y] + int(62*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                0,
                2080,
                int(58 * 1.6),
                int(62 * 1.6),
                self.camera[X] + int(58 * 1.6) // 2,
                self.camera[Y] + int(62 * 1.6) // 2
            )

next_state = {
    IDLE: {WD: JUMP, AD: WALK, AU: WALK, DD: WALK, DU: WALK},
    WALK: {WD: JUMP, AD: IDLE, AU: IDLE, DD: IDLE, DU: IDLE, SHIFTD: RUN, SHIFTU: RUN},
    RUN: {WD: JUMP, AD: IDLE, AU: IDLE, DD: IDLE, DU: IDLE, SHIFTD: WALK, SHIFTU: WALK},
    JUMP: {AD:JUMP,AU:JUMP,DD:JUMP,DU:JUMP},
    FALL: {AD: FALL, AU: FALL, DD: FALL, DU: FALL}
}
yoshi_delay = {IDLE_01:8,IDLE_02:10,WALK:8,RUN: 8,JUMP:0,FALL:0}
yoshi_motion_num = {IDLE_01:8,IDLE_02:5, WALK:8, RUN:2, JUMP:1, FALL:1}


class Yoshi:
    def __init__(self):
        self.image = [load_image("yoshi_mario.png")]
        # 위치 관련
        self.x = 4000
        self.y = 1500
        self.size = [int(62 * 1.6), int(66 * 1.6)]

        # 상태 관련
        self.state = "MARIO"
        self.frame = 0
        self.delay = 0

        # 이동 관련
        self.dir = [0, 0]
        self.speed = 5
        self.gravity = -GRAVITY

        # 카메라 관련
        self.camera = [0, 0]

        # 점프 관련
        self.pressJump = False

        # 상태 관련(리팩토링중)
        self.event_que = []
        self.cur_state = IDLE
        self.face = LEFT
        self.cur_state.enter(self)

    def sprite_update(self):
        if self.delay >= yoshi_delay[self.cur_state] :
            self.frame = (self.frame+1)%yoshi_motion_num[self.cur_state]
            self.delay = 0
            if self.cur_state==IDLE_01 and self.frame == 0:
                if random.randint(0, 3) == 0:
                    self.cur_state.exit(self)
                    self.cur_state = IDLE_02
                    self.cur_state.enter(self)
            if self.cur_state==IDLE_02 and self.frame == 0:
                self.cur_state.exit(self)
                self.cur_state = IDLE_01
                self.cur_state.enter(self)
        else:
            self.delay += 1