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

    def draw(self):
        self.cur_state.draw(self)

    def update(self):
        self.sprite_update()
        self.calc_gravity()
        self.calc_jump()
        self.move()
        self.check_camera()

        self.cur_state.do(self)

    def check_camera(self):
        from play_state import stageState
        if self.state == "MARIO":
            self.camera[X] = stageState.cameraSize[X] // 2
            self.camera[Y] = stageState.cameraSize[Y] // 2
            if self.x < stageState.cameraSize[X] // 2:  # 맵 왼편
                self.camera[X] = self.x
            if self.y < stageState.cameraSize[Y] // 2:  # 맵 아래편
                self.camera[Y] = self.y

            # 맵 오른편 위편
            if self.x > stageState.image[stageState.selectStage].w - stageState.cameraSize[X] // 2:
                self.camera[X] = stageState.cameraSize[X] - (stageState.image[stageState.selectStage].w - self.x)
            if self.y > stageState.image[stageState.selectStage].h - stageState.cameraSize[Y] // 2:
                self.camera[Y] = stageState.cameraSize[Y] - (stageState.image[stageState.selectStage].h - self.y)

    def calc_jump(self):#TODO: 점프중에만 적용되도록 설정
        from play_state import stageState
        #TODO: 나중에 game_world 에 넣어서 한번에 꺼내쓸수 있도록 해보기
        for rect in stageState.largerBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.bottom - self.size[Y] - 1
                self.gravity = 0
                rect.larger_block = True
                #TODO: 나중에 larger_block 상태 만들고서 치면 바뀌게 하기
        for rect in stageState.footBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.bottom - self.size[Y] - 1
                self.gravity = 0
        for rect in stageState.ceilingBlock:
            if self.myIntersectRect(rect):
                self.y = rect.bottom - self.size[Y] - 2
                self.gravity = 0

    def calc_gravity(self):
        global GRAVITY
        self.y += self.gravity
        self.gravity -= GRAVITY
        if self.gravity < -GRAVITY * 3:
            self.gravity = -GRAVITY * 3
        #TODO: check_fall 함수 이름을 check_landing 으로 바꾸기
        from play_state import stageState
        for rect in stageState.jumpBlock:
            if self.y - self.gravity >= rect.pos.top:
                if self.myIntersectRect(rect.pos):
                    self.y = rect.pos.top
                    self.gravity = rect.jump_power
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
                self.gravity = -GRAVITY;
                if self.cur_state == FALL:
                    self.check_fall()
        for rect in stageState.stairRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
                self.gravity = -GRAVITY;
                if self.cur_state == FALL:
                    self.check_fall()
        for rect in stageState.largerBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.top
                self.gravity = -GRAVITY
                if self.cur_state == FALL:
                    self.check_fall()
        for rect in stageState.footBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.top
                self.gravity = -GRAVITY;
                if self.cur_state == FALL:
                    self.check_fall()

    def check_fall(self):
        if self.dir[X] == 0:
            self.cur_state.exit(self)
            self.cur_state = IDLE
            self.cur_state.enter(self)
        else:
            self.cur_state.exit(self)
            self.cur_state = WALK
            self.cur_state.enter(self)

    def myIntersectRect(self, rect ):
        if rect.left == -1: return
        bVertical = False
        bHorizontal = False

        if self.x < rect.right and self.x+self.size[X] > rect.left:
            bHorizontal=True

        if self.y+self.size[Y] > rect.bottom and self.y < rect.top:
            bVertical = True

        if bVertical and bHorizontal:
            return True
        else:
            return False

    def move(self):
        self.x += self.dir[X] * self.speed
        if self.cur_state==RUN:
            self.x += self.dir[X] * self.speed // 2
        from play_state import stageState
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                if self.dir[X] == 1:
                    self.x = rect.left - self.size[X]
                elif self.dir[X] == -1:
                    self.x = rect.right
        for rect in stageState.largerBlock:
            if self.myIntersectRect(rect.pos):
                if self.dir[X] == 1:
                    self.x = rect.pos.left - self.size[X]
                elif self.dir[X] == -1:
                    self.x = rect.pos.right
        for rect in stageState.footBlock:
            if self.myIntersectRect(rect.pos):
                if self.dir[X] == 1:
                    self.x = rect.pos.left - self.size[X]
                elif self.dir[X] == -1:
                    self.x = rect.pos.right
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0


        #TODO: 나중에 다시 읽고 리팩토링이 되도록 설정하기
    def check_jump(self):
        global GRAVITY, MAXJUMPTIME, jump_delay
        if self.pressJump != 0:
            if self.pressJump <=MAXJUMPTIME:
                if jump_delay == 0:
                    if self.gravity==-GRAVITY: self.gravity+=GRAVITY*4
                    else :self.gravity += GRAVITY*2
                    self.pressJump+=1
                jump_delay = (jump_delay+1) % 3
            else:
                self.pressJump=0
                jump_delay=0
                if self.motion == "LEFT_JUMP":
                    self.change_motion("LEFT_FALL")
                    self.cur_state.exit(self)
                    self.cur_state= FALL
                    self.cur_state.enter(self)
                elif self.motion == "RIGHT_JUMP":
                    self.change_motion("RIGHT_FALL")
                    self.cur_state.exit(self)
                    self.cur_state = FALL
                    self.cur_state.enter(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        if self.event_que:
            event = self.event_que.pop()
            if event in next_state[self.cur_state]:
                self.cur_state.exit(self, event)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)


