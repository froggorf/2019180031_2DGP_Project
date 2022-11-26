from pico2d import *
import random
import game_framework
import finish_state
import game_world
import play_state
import item

yoshi_state = {"MARIO": 0 , "NOMARIO":1, "MARIO_SWALLOW":2, "NOMARIO_SWALLOW":3}
X = 0
Y = 1
LEFT = 0
RIGHT = 1
GRAVITY = 5
MAXJUMPTIME = 10
jump_delay = 0

#이벤트 정의
WD,WU,AD,AU,SD,SU,DD,DU,SHIFTD,SHIFTU,GOTOFLY,CTRLD,CTRLU,ED,EU = range(15)
key_down = [False for i in range(15)]

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
    (SDL_KEYDOWN, SDLK_LCTRL): CTRLD,
    (SDL_KEYDOWN,SDLK_e):ED,
    (SDL_KEYUP,SDLK_e):EU
}

class IDLE_01:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):
        pass

    def draw(self):
        if self.state == "MARIO":
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
        elif self.state == "NOMARIO":
            if self.face == RIGHT:  # RIGHT
                self.image[yoshi_state[self.state]].clip_draw(
                    int(54 * 1.6) * self.frame,
                    0,
                    int(54 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(54 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(54 * 1.6) * self.frame,
                    160,
                    int(54 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(54 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )


class IDLE_02:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0
        pass

    def exit(self, event=None):
        pass

    def do(self):
        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:  # RIGHT
                self.image[yoshi_state[self.state]].clip_draw(
                    int(62 * 1.6) * self.frame,
                    320,
                    int(62 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(62 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(62 * 1.6) * self.frame,
                    480,
                    int(62 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(62 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:  # RIGHT
                self.image[yoshi_state[self.state]].clip_draw(
                    int(42 * 1.6) * self.frame,
                    320,
                    int(42 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(42 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(42 * 1.6) * self.frame,
                    480,
                    int(42 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(42 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )

class WALK:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        if event == DD:
            self.dir[X] += 1
            self.face = RIGHT
        elif event == AD:
            self.dir[X] -= 1
            self.face = LEFT
        elif event == DU:
            self.dir[X] -= 1
            self.face = LEFT
        elif event == AU:
            self.dir[X] += 1
            self.face = RIGHT


    def exit(self, event=None):
        pass

    def do(self):

        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(64 * 1.6) * self.frame,
                    640,
                    int(64 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(64 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(64 * 1.6) * self.frame,
                    800,
                    int(64 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(64 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(52 * 1.6) * self.frame,
                    640,
                    int(52 * 1.6),
                    int(62 * 1.6),
                    self.camera[X] + int(52 * 1.6) // 2,
                    self.camera[Y] + int(62 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(52 * 1.6) * self.frame,
                    800,
                    int(52 * 1.6),
                    int(62 * 1.6),
                    self.camera[X] + int(52 * 1.6) // 2,
                    self.camera[Y] + int(62 * 1.6) // 2
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
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(72 * 1.6) * self.frame,
                    960,
                    int(72 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(72 * 1.6) * self.frame,
                    1120,
                    int(72 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(72 * 1.6) * self.frame,
                    960,
                    int(72 * 1.6),
                    int(52 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(52 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(72 * 1.6) * self.frame,
                    1120,
                    int(72 * 1.6),
                    int(52 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(52 * 1.6) // 2
                )

class JUMP:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        if event == WD and self.gravity < 10:
            self.gravity += GRAVITY*5
            self.pressJump += 1

        if event == DD:
            self.dir[X]+=1
            self.face = RIGHT
        elif event == AD:
            self.dir[X]-=1
            self.face = LEFT
        elif event == DU:
            self.dir[X] -= 1
            if key_down[AD] == True:
                self.face = LEFT
        elif event == AU:
            self.dir[X] += 1
            if key_down[DD] == True:
                self.face= RIGHT

    def exit(self, event=None):
        self.pressJump = 0

        pass

    def do(self):
        self.check_jump()
        if self.gravity<0:
            self.cur_state.exit(self)
            self.cur_state = FALL
            self.cur_state.enter(self)
        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1600,
                    int(60 * 1.6),
                    int(72 * 1.6),
                    self.camera[X] + int(60 * 1.6) // 2,
                    self.camera[Y] + int(72 * 1.6) // 2
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
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1600,
                    int(50 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(50 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1760,
                    int(50 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(50 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )

class FALL:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        if event == DD:
            self.dir[X]+=1
            self.face = RIGHT
        elif event == AD:
            self.dir[X]-=1
            self.face = LEFT
        elif event == DU:
            self.dir[X] -= 1
            if key_down[AD] == True:
                self.face = LEFT
        elif event == AU:
            self.dir[X] += 1
            if key_down[DD] == True:
                self.face= RIGHT
    def exit(self, event=None):
        self.pressJump = 0
        pass

    def do(self):
        if self.flytime <0 :
            self.flytime+=1

        if self.flytime == 0 and key_down[WD]:
            self.cur_state.exit(self)
            self.cur_state = FLY
            self.cur_state.enter(self,GOTOFLY)
        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1920,
                    int(58 * 1.6),
                    int(62 * 1.6),
                    self.camera[X] + int(58 * 1.6) // 2,
                    self.camera[Y] + int(62 * 1.6) // 2
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
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1920,
                    int(46 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(46 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    2080,
                    int(46 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(46 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )

#TODO: FALL 중일때도 FLY로 넘어갈 수 있게 하기
fly_gravity = [0,4,4,0,-4,-4,-2,2,10]
class FLY:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        if event == GOTOFLY:
            self.flytime = 0
        if event == DD:
            self.dir[X] += 1
            self.face = RIGHT
        elif event == AD:
            self.dir[X] -= 1
            self.face = LEFT
        elif event == DU:
            self.dir[X] -= 1
            if key_down[AD] == True:
                self.face = LEFT
        elif event == AU:
            self.dir[X] += 1
            if key_down[DD] == True:
                self.face = RIGHT

    def exit(self, event=None):
        if event == WU:
            self.flytime = -35
            self.gravity = 0
        pass

    def do(self):
        self.flytime = (self.flytime+1)
        if self.flytime == 90:
            self.cur_state.exit(self, WU)
            self.cur_state = FALL
            self.cur_state.enter(self)
        else:
            self.gravity = fly_gravity[self.flytime//10]
        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(62 * 1.6) * self.frame,
                    1280,
                    int(62 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(62 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(62 * 1.6) * self.frame,
                    1440,
                    int(62 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(62 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(50 * 1.6) * self.frame,
                    1280,
                    int(50 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(50 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(50 * 1.6) * self.frame,
                    1440,
                    int(50 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(50 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )

class TONGUE_ATTACK:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0

        play_state.tongue = Tongue(self.face,self.x,self.y)
        play_state.spawnTongue = True
        self.attack_time = 0

    def exit(self, event=None):
        if play_state.tongue.eatting:
            self.egg_count+=1
            if self.egg_count>9:
                self.egg_count = 9
            print(self.egg_count)

        game_world.remove_object(play_state.tongue)

        if(key_down[DD] and key_down[AD]):
            self.cur_state = IDLE_01
            self.cur_state.enter(self)
        elif key_down[DD]:
            self.cur_state = WALK
            self.cur_state.enter(self,DD)
        elif key_down[AD]:
            self.cur_state = WALK
            self.cur_state.enter(self, AD)
        else:
            self.cur_state = IDLE_01
            self.cur_state.enter(self)

    def do(self):
        self.attack_time+=1
        if self.attack_time>27+5+27+1:
            self.cur_state.exit(self)

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(68 * 1.6) * self.frame,
                    self.image[yoshi_state[self.state]].h-328,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(68 * 1.6) * self.frame,
                    self.image[yoshi_state[self.state]].h - 168,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )

class EGG_ATTACK_START:
    aiming_line_img = None
    def enter(self, event=None):
        if self.egg_count <= 0:
            self.dir[X] = 0
            self.cur_state.exit(self)
            return
        if EGG_ATTACK_START.aiming_line_img == None:
            EGG_ATTACK_START.aiming_line_img = load_image('aiming_line.png')
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0

        self.degree = 0
        self.radian = 0
        self.forward = True

        pass

    def exit(self, event=None):
        if event == ED: return
        if (key_down[DD] and key_down[AD]):
            self.cur_state = IDLE_01
            self.cur_state.enter(self)
        elif key_down[DD]:
            self.cur_state = WALK
            self.cur_state.enter(self, DD)
        elif key_down[AD]:
            self.cur_state = WALK
            self.cur_state.enter(self, AD)
        else:
            self.cur_state = IDLE_01
            self.cur_state.enter(self)

    def do(self):
        if self.forward:
            self.degree -= 2
            if self.degree <= -70:
                self.degree = -70
                self.forward = False
        else:
            self.degree += 2
            if self.degree >= 70:
                self.degree = 70
                self.forward = True

        self.radian = 3.141592*self.degree/180


    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(68 * 1.6) * self.frame,
                    self.image[yoshi_state[self.state]].h-328,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
            EGG_ATTACK_START.aiming_line_img.clip_composite_draw(
                0,
                0,
                EGG_ATTACK_START.aiming_line_img.w,
                EGG_ATTACK_START.aiming_line_img.h,
                self.radian,
                '',
                self.camera[X]+int(68 * 1.6),
                self.camera[Y]+EGG_ATTACK_START.aiming_line_img.h//2,
                #get_canvas_width()//2,
                #get_canvas_height()//2
            )
        else:
          self.image[yoshi_state[self.state]].clip_draw(
                int(68 * 1.6) * self.frame,
                self.image[yoshi_state[self.state]].h - 168,
                int(68 * 1.6),
                int(64 * 1.6),
                self.camera[X] + int(68 * 1.6) // 2,
                self.camera[Y] + int(64 * 1.6) // 2
            )

class EGG_ATTACK_END:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        print(self.degree)
        pass

    def exit(self, event=None):
        if (key_down[DD] and key_down[AD]):
            self.cur_state = IDLE_01
            self.cur_state.enter(self)
        elif key_down[DD]:
            self.cur_state = WALK
            self.cur_state.enter(self, DD)
        elif key_down[AD]:
            self.cur_state = WALK
            self.cur_state.enter(self, AD)
        else:
            self.cur_state = IDLE_01
            self.cur_state.enter(self)

    def do(self):
        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(68 * 1.6) * self.frame,
                    self.image[yoshi_state[self.state]].h - 328,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
        else:
            self.image[yoshi_state[self.state]].clip_draw(
                int(68 * 1.6) * self.frame,
                self.image[yoshi_state[self.state]].h - 168,
                int(68 * 1.6),
                int(64 * 1.6),
                self.camera[X] + int(68 * 1.6) // 2,
                self.camera[Y] + int(64 * 1.6) // 2
            )






next_state = {
    IDLE_01: {WD: JUMP, AD: WALK, AU: WALK, DD: WALK, DU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START},
    IDLE_02: {WD: JUMP, AD: WALK, AU: WALK, DD: WALK, DU: WALK, CTRLD:TONGUE_ATTACK, ED:EGG_ATTACK_START},
    WALK: {WD: JUMP, AD: IDLE_01, AU: IDLE_01, DD: IDLE_01, DU: IDLE_01, SHIFTD: RUN, SHIFTU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START},
    RUN: {WD: JUMP, AD: IDLE_01, AU: IDLE_01, DD: IDLE_01, DU: IDLE_01, SHIFTD: WALK, SHIFTU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START},
    JUMP: {WD: JUMP, WU:FALL,AD: JUMP, AU: JUMP, DD: JUMP, DU: JUMP},
    FALL: {AD: FALL, AU: FALL, DD: FALL, DU: FALL},
    FLY: {WU: FALL, AD:FLY, AU: FLY, DD: FLY, DU:FLY},
    TONGUE_ATTACK:{},
    EGG_ATTACK_START:{ED: EGG_ATTACK_END},
    EGG_ATTACK_END:{}
}
yoshi_delay = {IDLE_01:8,IDLE_02:10,WALK:8,RUN: 8,JUMP:0,FALL:0, FLY: 6,TONGUE_ATTACK: 10,EGG_ATTACK_START:10,EGG_ATTACK_END: 10}
yoshi_motion_num = {IDLE_01:8,IDLE_02:5, WALK:8, RUN:2, JUMP:1, FALL:1, FLY: 8, TONGUE_ATTACK:1,EGG_ATTACK_START:1,EGG_ATTACK_END:1}

class Tongue:
    tongueImg = None
    def __init__(self, face,x,y):
        self.face = face
        self.x = x
        self.y=y
        self.attack_time = 0
        self.tongue_length = 0
        self.eatting = False
        if Tongue.tongueImg == None:
            Tongue.tongueImg = load_image("tongue.png")
        pass
    def draw(self,left,bottom,right,top):
        if self.face == RIGHT:
            #self.x - left + self.size[X] // 2,
            self.tongueImg.clip_draw_to_origin(
                self.tongueImg.w - self.tongue_length,
                self.tongueImg.h // 2,
                self.tongue_length,
                self.tongueImg.h // 2,
                self.x - left+80,
                self.y - bottom+22
            )
            # self.tongueImg.clip_draw(
            #
            #
            # )
        else:
            self.tongueImg.clip_draw_to_origin(
                0,
                0,
                self.tongue_length,
                self.tongueImg.h // 2,
                self.x-left-self.tongue_length+30,
                self.y-bottom+22
            )

        pass

    def update(self):
        self.attack_time += 1
        if self.attack_time <= 27:
            self.tongue_length += 10
            if (self.tongue_length >= self.tongueImg.w):
                self.tongue_length = self.tongueImg.w

        elif self.attack_time <= 27 + 5:
            pass
        elif self.attack_time <= 27 + 5 + 27+1:
            self.tongue_length -= 10
            if (self.tongue_length < 0):
                self.tongue_length = 0
        else:
            pass

    def get_bb(self):
        if self.face==RIGHT:
            return self.x+80,self.y,self.x+self.tongue_length+80,self.y+self.tongueImg.h//2
        else:
            return self.x- self.tongue_length+30, self.y, self.x+30 , self.y + self.tongueImg.h // 2

        pass

    def handle_collision(self, other, group):
        if other == self: return

        if group == 'tongue:enemies':
            other.grabbed = True
            if self.tongue_length == 0:
                self.eatting = True
                game_world.remove_object(other)
            if self.face == RIGHT:
                other.x = self.x+30+self.tongue_length-10
                other.y = self.y
            else:
                other.x = self.x+25-self.tongue_length+5
                other.y=self.y
        pass




class Yoshi:
    def __init__(self):
        self.image = [load_image("yoshi_temp.png"),load_image("test.png")]

        # 위치 관련
        self.x = 5200
        self.y = 3000
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

        # 점프/날기 관련
        self.pressJump = False
        self.flytime = 0


        # 상태 관련(리팩토링중)
        self.event_que = []
        self.cur_state = FALL
        self.face = RIGHT
        self.cur_state.enter(self)

        self.egg_count = 0

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

    def draw(self,temp1,temp2,temp3,temp4):
        self.check_camera()
        self.cur_state.draw(self)

    def update(self):
        self.sprite_update()

        self.cur_state.do(self)
        self.move()
        self.calc_gravity()

        #TODO: 나중에 game_world만들고 충돌체크 처리하기
        #self.collide_enemy()


        # self.check_finish()


    def check_camera(self):
        from play_state import stageState
        #if self.state == "MARIO":
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



    def calc_gravity(self):
        self.y += self.gravity
        #TODO: 나중에 지우기
        if self.y<0:
            self.y = 0
        self.gravity -= GRAVITY
        if self.gravity < -GRAVITY * 3:
            if self.cur_state != FALL and self.cur_state!= FLY:
                self.cur_state.exit(self)
                self.flytime = 0
                self.cur_state = FALL
                self.cur_state.enter(self)
            self.gravity = -GRAVITY * 3


    def check_fall(self):
        if self.dir[X] == 0:
            self.cur_state.exit(self)
            self.cur_state = IDLE_01
            self.cur_state.enter(self)
        elif key_down[AD] or key_down[DD] or self.dir[X] != 0:
            self.cur_state.exit(self)
            self.cur_state = WALK
            self.cur_state.enter(self)
        else:
            print('Error - 일어날 수 없음')

    #TODO: game_world 리팩토링 진행하기
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

        for rect in play_state.groundRect:
            if play_state.collide(play_state.yoshi,rect):
                if self.dir[X] == 1:
                    self.x = rect.left - self.size[X] - 1
                elif self.dir[X] == -1:
                    self.x = rect.right + 1
        for rect in play_state.largeBlock:
            if play_state.collide(play_state.yoshi,rect):
                if self.dir[X] == 1:
                    self.x = rect.pos.left - self.size[X] - 1
                elif self.dir[X] == -1:
                    self.x = rect.pos.right + 1
        for rect in play_state.footBlock:
            if play_state.collide(play_state.yoshi,rect):
                if self.dir[X] == 1:
                    self.x = rect.pos.left - self.size[X] - 1
                elif self.dir[X] == -1:
                    self.x = rect.pos.right+ 1

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0


        #TODO: 나중에 다시 읽고 리팩토링이 되도록 설정하기
    def check_jump(self):
        global jump_delay
        if self.pressJump != 0:
            if self.pressJump <=MAXJUMPTIME:
                if jump_delay == 0:
                    if self.gravity==-GRAVITY: self.gravity+=GRAVITY*4
                    else :
                        self.gravity += GRAVITY*2
                    self.pressJump+=1
                jump_delay = (jump_delay+1) % 3
            else:
                self.pressJump=0
                jump_delay=0
                self.cur_state.exit(self)
                self.cur_state= FLY
                self.cur_state.enter(self,GOTOFLY)

    def collide_enemy(self):
        from play_state import enemies
        from stage import myRect
        a = myRect(enemies.x, enemies.y, enemies.x+60,enemies.y+80)
        if self.myIntersectRect(a):
            if self.state == "MARIO":
                self.state = "NOMARIO"
                play_state.stageState.babymario = item.BabyMario(self.x-80,self.y+80)
    def check_finish(self):
        pass
        # from play_state import stageState
        # if self.myIntersectRect(stageState.finishLine):
        #     self.cur_state= WALK
        #     game_framework.push_state(finish_state)
    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        if self.event_que:
            event = self.event_que.pop()
            set_keydown(event)
            if event in next_state[self.cur_state]:
                self.cur_state.exit(self, event)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

    def get_bb(self):
        return self.x, self.y, self.x+self.size[X], self.y+self.size[Y]

    def handle_collision(self,other,group):
        #print('yoshi 가 무언가랑 만났다고 함')
        if other == self : return

        if group == 'yoshi:groundRect':
            self.y = other.top+ 1
            self.gravity = -GRAVITY;
            if self.cur_state == FALL:
                self.check_fall()
        elif group == 'yoshi:stairRect':
            self.y = other.top+ 1
            self.gravity = -GRAVITY;
            if self.cur_state == FALL:
                self.check_fall()
        elif group == 'yoshi:ceilingBlock':
            if self.gravity>= 0:
                self.y = other.bottom - self.size[Y] - 2
                self.gravity = 0
        elif group == 'yoshi:largeBlock':
            if self.gravity >= 0:
                self.y = other.pos.bottom - self.size[Y] - 1
                self.gravity = 0
                other.larger_block = True
            else:
                self.y = other.pos.top + 1
                self.gravity = -GRAVITY
                if self.cur_state == FALL:
                    self.check_fall()
        elif group == 'yoshi:footBlock':
            for rect in play_state.largeBlock:
                if play_state.collide(self, rect):
                    self.handle_collision(rect,'yoshi:largeBlock')
            if self.gravity>=0:
                self.y = other.pos.bottom - self.size[Y] - 1
                self.gravity = 0
            else:
                self.y = other.pos.top + 1
                self.gravity = -GRAVITY;
                if self.cur_state == FALL:
                    self.check_fall()
        elif group == 'yoshi:jumpBlock':
            if self.y - self.gravity >= other.pos.top:
                    self.y = other.pos.top
                    self.gravity = other.jump_power
                    self.pressJump = MAXJUMPTIME
                    self.cur_state.exit(self)
                    self.cur_state = JUMP
                    self.cur_state.enter(self)
        elif group == 'yoshi:coins':
            game_world.remove_object(other)
        elif group == 'yoshi:finishLine':
            self.cur_state = WALK
            game_framework.push_state(finish_state)
        elif group == 'yoshi:enemies':
            if other.grabbed: return
            if self.state == "MARIO":
                self.state = "NOMARIO"
                play_state.babyMario = item.BabyMario(self.x-130,self.y+100)
                play_state.spawnMario = True
        elif group == 'yoshi:babyMario':
            play_state.yoshi.state='MARIO'
            game_world.remove_object(other)




#TODO: 좋은 방법 생각나면 리팩토링 하기
def set_keydown(event):
    if event == WD:
        key_down[WD]=True
    elif event==WU:
        key_down[WD] = False
    elif event == AD:
        key_down[AD] = True
    elif event == AU:
        key_down[AD] = False
    elif event == SD:
        key_down[SD] = True
    elif event == SU:
        key_down[SD] = False
    elif event == DD:
        key_down[DD] = True
    elif event == DU:
        key_down[DD] = False
    elif event == SHIFTD:
        key_down[SHIFTD] = True
    elif event == SHIFTU:
        key_down[SHIFTD] = False
    elif event == CTRLD:
        key_down[CTRLD] = True
    elif event == CTRLU:
        key_down[CTRLU] = False
    elif event == ED:
        key_down[ED] = True
    elif event== EU:
        key_down[ED] = False



