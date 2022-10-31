from pico2d import *
import random

yoshi_state = {"MARIO": 0 , "NOMARIO":1, "MARIO_SWALLOW":2, "NOMARIO_SWALLOW":3}
yoshi_motion = {"RIGHT_IDLE_01":0, "LEFT_IDLE_01":1,"RIGHT_IDLE_02":2,"LEFT_IDLE_02":3, "RIGHT_WALK":4,"LEFT_WALK":5, "RIGHT_RUN":6, "LEFT_RUN":7, "RIGHT_JUMP":10, "LEFT_JUMP":11, "RIGHT_FALL":12, "LEFT_FALL":13}
yoshi_offset = [
    [(int(62*1.6),int(66*1.6)),(int(62*1.6),int(66*1.6)),(int(62*1.6),int(64*1.6)),(int(62*1.6),int(64*1.6)),(int(64*1.6),int(66*1.6)),(int(64*1.6),int(66*1.6)),(int(72*1.6),int(1.6*68)),(int(72*1.6),int(1.6*68)),(),(),(int(60*1.6),int(72*1.6)),(int(60*1.6),int(72*1.6)),(int(58*1.6),int(62*1.6)),(int(58*1.6),int(62*1.6))],
    [5],
    [5],
    [5]
]
yoshi_delay = [8,8,10,10,8,8,8,8,8,0,0,0,0,0,0]
yoshi_motion_num = [8,8,5,5,8,8,2,2,0,0,1,1,1,1]
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

class IDLE:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        print('enter - IDLE')
        pass

    def exit(self):
        print('exit - IDLE')
        pass

    def do(self):
        pass

    def draw(self):
        if yoshi_motion[self.motion]%2 ==0: #RIGHT
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
            pass
        pass

class WALK:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        print('enter - WALK')
        pass

    def exit(self):
        print('exit - WALK')
        pass

    def do(self):

        pass

    def draw(self):
        if yoshi_motion[self.motion]%2 == 0:
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
        pass

class RUN:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        print('enter - RUN')
        pass

    def exit(self):
        print('exit - RUN')
        pass

    def do(self):

        pass

    def draw(self):
        if yoshi_motion[self.motion]%2==0:
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
        pass

class JUMP:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        print('enter - JUMP')
        pass

    def exit(self):
        print('exit - JUMP')

    def do(self):
        if self.gravity < -GRAVITY:
            self.cur_state.exit(self)
            self.cur_state = FALL
            self.cur_state.enter(self)
        pass

    def draw(self):
        if yoshi_motion[self.motion]%2 == 0:
            self.image[yoshi_state[self.state]].clip_draw(
                int(60*1.6) * self.frame,
                1600,
                int(60*1.6),
                int(72*1.6),
                self.camera[X] + int(60*1.6) // 2,
                self.camera[Y] + int(72*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(60 * 1.6) * self.frame,
                1760,
                int(60 * 1.6),
                int(72 * 1.6),
                self.camera[X] + int(60 * 1.6) // 2,
                self.camera[Y] + int(72 * 1.6) // 2
            )
        pass

class FALL:
    def enter(self, event=None):
        print('enter - FALL')
        self.delay = 0
        self.frame = 0
        pass

    def exit(self):
        print('exit - FALL')
        pass

    def do(self):
        pass

    def draw(self):
        if yoshi_motion[self.motion] %2 ==0:
            self.image[yoshi_state[self.state]].clip_draw(
                int(58*1.6) * self.frame,
                1920,
                int(58*1.6),
                int(62*1.6),
                self.camera[X] + int(58*1.6) // 2,
                self.camera[Y] + int(62*1.6) // 2
            )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(58 * 1.6) * self.frame,
                2080,
                int(58 * 1.6),
                int(62 * 1.6),
                self.camera[X] + int(58 * 1.6) // 2,
                self.camera[Y] + int(62 * 1.6) // 2
            )

next_state = {
    IDLE: {WD: JUMP, WU: JUMP, AD: WALK, AU: WALK, SD: IDLE, SU: IDLE, DD: WALK, DU: WALK, SHIFTD: IDLE, SHIFTU: IDLE},
    WALK: {WD: JUMP, WU: JUMP, AD: IDLE, AU: IDLE, SD: WALK, SU: WALK, DD: IDLE, DU: IDLE, SHIFTD: RUN, SHIFTU: RUN},
    RUN: {WD: JUMP, WU: JUMP, AD: IDLE, AU: IDLE, SD: RUN, SU: RUN, DD: IDLE, DU: IDLE, SHIFTD: WALK, SHIFTU: WALK},
    JUMP: {WD: JUMP, WU: JUMP, AD: JUMP, AU: JUMP, SD: JUMP, SU: JUMP, DD: JUMP, DU: JUMP, SHIFTD: JUMP, SHIFTU: JUMP},
    FALL: {WD: FALL, WU: FALL, AD: FALL, AU: FALL, SD: FALL, SU: FALL, DD: FALL, DU: FALL, SHIFTD: FALL, SHIFTU: FALL}
}

class Yoshi:
    def __init__(self):
        self.image = [load_image("yoshi_mario.png")]
        #위치 관련
        self.x = 2400
        self.y = 320
        self.size=[int(62*1.6),int(66*1.6)]

        #상태 관련
        self.state = "MARIO"
        self.motion = "RIGHT_IDLE_02"
        self.frame = 0
        self.delay = 0
        #self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]

        #이동 관련
        self.dir = [0, 0]
        self.speed = 5
        self.gravity = -GRAVITY

        #카메라 관련
        self.camera = [0,0]

        #점프 관련
        self.pressJump = False

        #상태 관련(리팩토링중)
        self.event_que = []
        self.cur_state = IDLE
        self.face = LEFT
        self.cur_state.enter(self)

    #그리기 관련 함수
    def sprite_update(self):
        if self.delay >= yoshi_delay[yoshi_motion[self.motion]] :
            self.frame = (self.frame+1)%yoshi_motion_num[yoshi_motion[self.motion]]
            self.delay = 0
            if (self.motion == "RIGHT_IDLE_01" or self.motion == "RIGHT_IDLE_02") and self.frame == 0:
                if random.randint(0, 3) == 0:
                    self.change_motion("RIGHT_IDLE_02")
                else:
                    self.change_motion("RIGHT_IDLE_01")
            elif (self.motion == "LEFT_IDLE_01" or self.motion == "LEFT_IDLE_02") and self.frame == 0:
                if random.randint(0, 3) == 0:
                    self.change_motion("LEFT_IDLE_02")
                else:
                    self.change_motion("LEFT_IDLE_01")
        else:
            self.delay += 1

    def draw(self):
        self.cur_state.draw(self)
        pass



    def update(self):
        #self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]
        #if self.dir[X] == 1:

        self.sprite_update()
        self.check_jump()
        self.calc_gravity()
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

    def change_motion(self, c_motion):
        self.motion = c_motion
        # self.delay = 0
        # self.frame = 0

    def calc_gravity(self):
        global GRAVITY
        self.y += self.gravity
        self.gravity -= GRAVITY
        if self.gravity < -GRAVITY*3:
            self.gravity = -GRAVITY*3

        from play_state import stageState
        if self.gravity<=0:     #중력 적용중일때
            for rect in stageState.jumpBlock:
                if self.y-self.gravity>=rect.pos.top:
                    if self.myIntersectRect(rect.pos):
                        self.y = rect.pos.top
                        self.gravity = rect.jump_power
                        if self.motion == "RIGHT_FALL" or self.motion == "RIGHT_JUMP":
                            self.change_motion("RIGHT_JUMP")
                        else:
                            self.change_motion("LEFT_JUMP")
            for rect in stageState.groundRect:
                if self.myIntersectRect(rect):
                    self.y = rect.top
                    self.gravity=-GRAVITY;
                    if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                        self.check_fall()
            for rect in stageState.stairRect:
                if self.myIntersectRect(rect):
                    self.y = rect.top
                    self.gravity = -GRAVITY;
                    if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                        self.check_fall()
            for rect in stageState.largerBlock:
                if self.myIntersectRect(rect.pos):
                    self.y = rect.pos.top
                    self.gravity = -GRAVITY
                    if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                        self.check_fall()
            for rect in stageState.footBlock:
                if self.myIntersectRect(rect.pos):
                    self.y = rect.pos.top
                    self.gravity = -GRAVITY;
                    if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                        self.check_fall()
        else:       #점프중일때
            for rect in stageState.largerBlock:
                if self.myIntersectRect(rect.pos):
                    self.y = rect.pos.bottom - self.size[Y]-1
                    self.gravity = 0
                    rect.larger_block=True
            for rect in stageState.footBlock:
                if self.myIntersectRect(rect.pos):
                    self.y = rect.pos.bottom - self.size[Y]-1
                    self.gravity = 0
            for rect in stageState.ceilingBlock:
                if self.myIntersectRect(rect):
                    self.y = rect.bottom - self.size[Y]-2
                    self.gravity= 0
            if self.gravity == 1:
                if self.motion == "RIGHT_JUMP":
                    self.motion = "RIGHT_FALL"
                elif self.motion == "LEFT_JUMP":
                    self.motion = "LEFT_FALL"



    def check_fall(self):
        if self.motion == "RIGHT_FALL":
            if self.dir[X] == 1:
                self.change_motion("RIGHT_WALK")
                self.cur_state.exit(self)
                self.cur_state=WALK
                self.cur_state.enter(self)
            else:
                self.change_motion("RIGHT_IDLE_01")
                self.cur_state.exit(self)
                self.cur_state = IDLE
                self.cur_state.enter(self)
        elif self.motion == "LEFT_FALL":
            if self.dir[X] == -1:
                self.change_motion("LEFT_WALK")
                self.cur_state.exit(self)
                self.cur_state = WALK
                self.cur_state.enter(self)
            else:
                self.change_motion("LEFT_IDLE_01")
                self.cur_state.exit(self)
                self.cur_state = IDLE
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
        if self.motion == "RIGHT_RUN" or self.motion == "LEFT_RUN":
            self.x += self.dir[X] * self.speed//2
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
        if self.x<0:
            self.x = 0
        if self.y<0:
            self.y=0

    def check_jump(self):
        global GRAVITY,MAXJUMPTIME, jump_delay
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

    def add_event(self,event):
        self.event_que.insert(0,event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self,event)
