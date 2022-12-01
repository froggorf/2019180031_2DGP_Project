from pico2d import *
import random
import game_framework
import finish_state
import game_world
import play_state
import item
yoshi_state = {"MARIO": 0 , "NOMARIO":1}
X = 0
Y = 1
LEFT = 0
RIGHT = 1
GRAVITY = 5
MAXJUMPTIME = 10
jump_delay = 0

#이벤트 정의
WD,WU,AD,AU,SD,SU,DD,DU,SHIFTD,SHIFTU,GOTOFLY,CTRLD,CTRLU,ED,EU,GETHIT = range(16)
key_down = [False for i in range(16)]

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
                    451+int(72 * 1.6) * self.frame,
                    960,
                    int(72 * 1.6),
                    int(68 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(68 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    int(72 * 1.6) * self.frame,
                    160*6,
                    int(72 * 1.6),
                    int(52 * 1.6),
                    self.camera[X] + int(72 * 1.6) // 2,
                    self.camera[Y] + int(52 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    469+int(72 * 1.6) * self.frame,
                    160*6,
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
            self.bgm_jump.play(1)

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
                    1120,
                    int(60 * 1.6),
                    int(72 * 1.6),
                    self.camera[X] + int(60 * 1.6) // 2,
                    self.camera[Y] + int(72 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    340,
                    1120,
                    int(60 * 1.6),
                    int(72 * 1.6),
                    self.camera[X] + int(60 * 1.6) // 2,
                    self.camera[Y] + int(72 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1120,
                    int(50 * 1.6),
                    int(66 * 1.6),
                    self.camera[X] + int(50 * 1.6) // 2,
                    self.camera[Y] + int(66 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    334,
                    1120,
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
                    1600,
                    int(58 * 1.6),
                    int(62 * 1.6),
                    self.camera[X] + int(58 * 1.6) // 2,
                    self.camera[Y] + int(62 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    325,
                    1600,
                    int(58 * 1.6),
                    int(62 * 1.6),
                    self.camera[X] + int(58 * 1.6) // 2,
                    self.camera[Y] + int(62 * 1.6) // 2
                )
        elif self.state == "NOMARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1600,
                    int(46 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(46 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    315,
                    1600,
                    int(46 * 1.6),
                    int(60 * 1.6),
                    self.camera[X] + int(46 * 1.6) // 2,
                    self.camera[Y] + int(60 * 1.6) // 2
                )

fly_gravity = [0,4,4,0,-4,-4,-2,2,10]
class FLY:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        if event == GOTOFLY:
            self.bgm_fly.set_volume(32)
            self.bgm_fly.play(1)
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
        self.bgm_fly.set_volume(0)
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
        self.bgm_tongue.play(1)
        play_state.tongue = Tongue(self.face,self.x,self.y)
        play_state.spawnTongue = True
        self.attack_time = 0

    def exit(self, event=None):
        if play_state.tongue.eatting!=0:
            self.egg_count+=play_state.tongue.eatting
            if self.egg_count>9:
                self.egg_count = 9

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
                    0,
                    1760,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    411,
                    1760,
                    int(68 * 1.6),
                    int(64 * 1.6),
                    self.camera[X] + int(68 * 1.6) // 2,
                    self.camera[Y] + int(64 * 1.6) // 2
                )
        else:
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1760,
                    93,
                    80,
                    self.camera[X] + 93 // 2,
                    self.camera[Y] + 80 // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    417,
                    1760,
                    93,
                    80,
                    self.camera[X] + 93 // 2,
                    self.camera[Y] + 80 // 2
                )

class EGG_ATTACK_START:
    aiming_line_img_right = None
    aiming_line_img_left = None
    def enter(self, event=None):
        if self.egg_count <= 0:
            self.dir[X] = 0
            self.cur_state.exit(self)
            return
        if EGG_ATTACK_START.aiming_line_img_right == None:
            EGG_ATTACK_START.aiming_line_img_right = load_image('resource\\about_yoshi\\aiming_line_right.png')
        if EGG_ATTACK_START.aiming_line_img_left == None:
            EGG_ATTACK_START.aiming_line_img_left = load_image('resource\\about_yoshi\\aiming_line_left.png')
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0

        self.degree = 0
        self.radian = 0
        self.forward = True
        self.aiming_time = 0
        self.bgm_aiming.set_volume(28)
        self.bgm_aiming.play(1)
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
        self.bgm_aiming.set_volume(0)

    def do(self):
        self.aiming_time += (1/60)
        if self.aiming_time >= 1:
            self.aiming_time = 0
            self.bgm_aiming.play(1)
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
                    0,
                    1920,
                    87,
                    103,
                    self.camera[X] + 87//2,
                    self.camera[Y] + 103//2
                )

                EGG_ATTACK_START.aiming_line_img_right.clip_composite_draw(
                    0,
                    0,
                    EGG_ATTACK_START.aiming_line_img_right.w,
                    EGG_ATTACK_START.aiming_line_img_right.h,
                    self.radian,
                    '',
                    self.camera[X]+int(68 * 1.6),
                    self.camera[Y]+EGG_ATTACK_START.aiming_line_img_right.h//2,
                )
            else:
              self.image[yoshi_state[self.state]].clip_draw(
                    361,
                    1920,
                    87,
                    103,
                    self.camera[X] + 87 // 2,
                    self.camera[Y] + 103 // 2
                )
              EGG_ATTACK_START.aiming_line_img_left.clip_composite_draw(
                  0,
                  0,
                  EGG_ATTACK_START.aiming_line_img_left.w,
                  EGG_ATTACK_START.aiming_line_img_left.h,
                  -self.radian,
                  '',
                  self.camera[X] ,
                  self.camera[Y] + EGG_ATTACK_START.aiming_line_img_left.h // 2,
              )
        else:
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    0,
                    1920,
                    84,
                    96,
                    self.camera[X] + 84//2,
                    self.camera[Y] + 96//2
                )

                EGG_ATTACK_START.aiming_line_img_right.clip_composite_draw(
                    0,
                    0,
                    EGG_ATTACK_START.aiming_line_img_right.w,
                    EGG_ATTACK_START.aiming_line_img_right.h,
                    self.radian,
                    '',
                    self.camera[X]+int(68 * 1.6),
                    self.camera[Y]+EGG_ATTACK_START.aiming_line_img_right.h//2,
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    363,
                    1920,
                    84,
                    96,
                    self.camera[X] + 84 // 2,
                    self.camera[Y] + 96 // 2
                )

                EGG_ATTACK_START.aiming_line_img_left.clip_composite_draw(
                    0,
                    0,
                    EGG_ATTACK_START.aiming_line_img_left.w,
                    EGG_ATTACK_START.aiming_line_img_left.h,
                    -self.radian,
                    '',
                    self.camera[X] ,
                    self.camera[Y] + EGG_ATTACK_START.aiming_line_img_left.h // 2,
                )


class EGG_ATTACK_END:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        self.bgm_egg_throwing.play(1)
        self.bgm_aiming.set_volume(0)

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
        if self.frame==3:
            play_state.eggs.append((item.Egg(int(self.x + self.size[X] // 2), int(self.y), self.radian, self.face)))
            play_state.spawnEgg = True
            self.egg_count -= 1
            if self.egg_count<=0:
                self.egg_count = 0
                print('error - egg_count is error')
            self.cur_state.exit(self)

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    106 * self.frame,
                    160*13,
                    106,
                    112,
                    self.camera[X] + 106 // 2,
                    self.camera[Y] + 112       // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    106 * self.frame,
                    160*14,
                    106,
                    112,
                    self.camera[X] + 106 // 2,
                    self.camera[Y] + 112 // 2
                )
        else:
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    105 * self.frame,
                    160*13,
                    106,
                    112,
                    self.camera[X] + 106 // 2,
                    self.camera[Y] + 112       // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    105 * self.frame,
                    160*14,
                    106,
                    112,
                    self.camera[X] + 106 // 2,
                    self.camera[Y] + 112 // 2
                )

class HITTING:
    def enter(self, event=None):
        self.delay = 0
        self.frame = 0
        self.dir[X] = 0
        self.hitting_time = 0
        self.bgm_hitting.play(1)
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
        self.image[yoshi_state['NOMARIO']].opacify(1)
        self.image[yoshi_state['MARIO']].opacify(1)
    def do(self):
        self.hitting_time+=1

        if self.hitting_time>=50:
            self.cur_state.exit(self)
        elif self.hitting_time>=25:
            if self.face == RIGHT:
                self.x -= 3
            else:
                self.x += 3
            self.y = self.y-3+self.gravity
        else:
            if self.face == RIGHT:
                self.x -= 3
            else:
                self.x += 3
            self.y =self.y+35+self.gravity
        if self.hitting_time%10 == 0:
            self.image[yoshi_state['NOMARIO']].opacify(1)
            self.image[yoshi_state['MARIO']].opacify(1)
        elif self.hitting_time%10 == 5:
            self.image[yoshi_state['NOMARIO']].opacify(0.5)
            self.image[yoshi_state['MARIO']].opacify(0.5)



        pass

    def draw(self):
        if self.state == "MARIO":
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    662,
                    160*14,
                    83,
                    99,
                    self.camera[X] + 83 // 2,
                    self.camera[Y] + 99       // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    777,
                    160*14,
                    83,
                    99,
                    self.camera[X] + 83 // 2,
                    self.camera[Y] + 99 // 2
                )
        else:
            if self.face == RIGHT:
                self.image[yoshi_state[self.state]].clip_draw(
                    738,
                    160*14,
                    81,
                    103,
                    self.camera[X] + 81 // 2,
                    self.camera[Y] + 103 // 2
                )
            else:
                self.image[yoshi_state[self.state]].clip_draw(
                    879,
                    160*14,
                    81,
                    103,
                    self.camera[X] + 81 // 2,
                    self.camera[Y] + 103 // 2
                )







next_state = {
    IDLE_01: {WD: JUMP, AD: WALK, AU: WALK, DD: WALK, DU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START,GETHIT:HITTING},
    IDLE_02: {WD: JUMP, AD: WALK, AU: WALK, DD: WALK, DU: WALK, CTRLD:TONGUE_ATTACK, ED:EGG_ATTACK_START,GETHIT:HITTING},
    WALK: {WD: JUMP, AD: IDLE_01, AU: IDLE_01, DD: IDLE_01, DU: IDLE_01, SHIFTD: RUN, SHIFTU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START,GETHIT:HITTING},
    RUN: {WD: JUMP, AD: IDLE_01, AU: IDLE_01, DD: IDLE_01, DU: IDLE_01, SHIFTD: WALK, SHIFTU: WALK,CTRLD:TONGUE_ATTACK,ED:EGG_ATTACK_START,GETHIT:HITTING},
    JUMP: {WD: JUMP, WU:FALL,AD: JUMP, AU: JUMP, DD: JUMP, DU: JUMP,GETHIT:HITTING},
    FALL: {AD: FALL, AU: FALL, DD: FALL, DU: FALL,GETHIT:HITTING},
    FLY: {WU: FALL, AD:FLY, AU: FLY, DD: FLY, DU:FLY,GETHIT:HITTING},
    TONGUE_ATTACK:{GETHIT:HITTING},
    EGG_ATTACK_START:{ED: EGG_ATTACK_END,GETHIT:HITTING},
    EGG_ATTACK_END:{GETHIT:HITTING},
    HITTING:{}
}
yoshi_delay = {IDLE_01:8,IDLE_02:10,WALK:8,RUN: 8,JUMP:0,FALL:0, FLY: 6,TONGUE_ATTACK: 10,EGG_ATTACK_START:10,EGG_ATTACK_END: 3,HITTING:10}
yoshi_motion_num = {IDLE_01:8,IDLE_02:5, WALK:8, RUN:2, JUMP:1, FALL:1, FLY: 8, TONGUE_ATTACK:1,EGG_ATTACK_START:1,EGG_ATTACK_END:4,HITTING:1}

class Tongue:
    tongueImg = None
    def __init__(self, face,x,y):
        self.face = face
        self.x = x
        self.y=y
        self.attack_time = 0
        self.tongue_length = 0
        self.eatting = 0
        if Tongue.tongueImg == None:
            Tongue.tongueImg = load_image("resource\\about_yoshi\\tongue.png")
        pass
    def draw(self,left,bottom,right,top):
        if self.face == RIGHT:
            if play_state.yoshi.state == "MARIO":
                self.tongueImg.clip_draw_to_origin(
                    self.tongueImg.w - self.tongue_length,
                    self.tongueImg.h // 2,
                    self.tongue_length,
                    self.tongueImg.h // 2,
                    self.x - left+80,
                    self.y - bottom+22
                )
            else:
                self.tongueImg.clip_draw_to_origin(
                    self.tongueImg.w - self.tongue_length,
                    self.tongueImg.h // 2,
                    self.tongue_length,
                    self.tongueImg.h // 2,
                    self.x - left + 70,
                    self.y - bottom + 22
                )

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
                self.eatting += 1
                game_world.remove_object(other)
                play_state.enemies.remove(other)
            if self.face == RIGHT:
                other.x = self.x+30+self.tongue_length-10
                other.y = self.y
            else:
                other.x = self.x+25-self.tongue_length+5
                other.y=self.y
        pass




class Yoshi:
    def __init__(self):
        self.image = [load_image("resource\\about_yoshi\\yoshi_with_mario_1.6x.png"),load_image("resource\\about_yoshi\\yoshi_1.6x.png")]

        # 위치 관련
        self.x = 2450
        self.y = 1400
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

        #개인 상태 관련
        self.egg_count = 0

        #사운드 관련
        self.bgm_jump = load_wav('resource\\sound\\yoshi_jump.wav')
        self.bgm_fly = load_wav('resource\\sound\\yoshi_flying.wav')
        self.bgm_tongue = load_wav('resource\\sound\\yoshi_tongue.wav')
        self.bgm_hitting = load_wav('resource\\sound\\yoshi_hitting.wav')
        self.bgm_egg_throwing = load_wav('resource\\sound\\yoshi_egg_throwing.wav')
        self.bgm_aiming = load_wav('resource\\sound\\yoshi_aiming.wav')


    def sprite_update(self):
        if self.delay >= yoshi_delay[self.cur_state] :
            self.frame = (self.frame+1)%yoshi_motion_num[self.cur_state]
            self.delay = 0
            if self.cur_state==IDLE_01 and self.frame == 0:
                if random.randint(0,2)==0:
                    self.cur_state.exit(self)
                    self.cur_state = IDLE_02
                    self.cur_state.enter(self)

            elif self.cur_state==IDLE_02 and self.frame==0:
                if random.randint(0,1)==0:
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




    def check_camera(self):
        from play_state import stageState
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

        if self.y<0:
            self.y = 0
        self.gravity -= GRAVITY
        if self.gravity < -GRAVITY * 3:
            if self.cur_state != FALL and self.cur_state!= FLY and self.cur_state!=RUN and self.cur_state != HITTING :
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


    def move(self):
        self.x += self.dir[X] * self.speed
        if self.cur_state==RUN:
            self.x += self.dir[X] * self.speed // 2

        for rect in play_state.groundRect:
            if play_state.collide(play_state.yoshi,rect):
                if self.dir[X] == 1:
                    self.x = rect.left - self.size[X] - 1
                elif self.dir[X] == -1:
                    self.x = rect.right + 3
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
        if other == self : return
        if group == 'yoshi:groundRect':
            if self.cur_state == HITTING and self.hitting_time<=24:
                self.y = other.bottom - self.size[Y]-1
                return
            if self.cur_state==FLY:
                if self.gravity == -9:
                    self.y = other.top+1
                elif self.gravity == -1:
                    self.y = other.bottom-self.size[Y]-1
                self.cur_state.exit(self)
                self.cur_state=FALL
                self.cur_state.enter(self)
                return
            if self.gravity>=0:
                self.y = other.bottom - self.size[Y]-1
                self.gravity = 0
                self.cur_state.exit(self)
                self.cur_state = FALL
                self.cur_state.enter(self)
            else:
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
            if self.cur_state == HITTING and self.hitting_time<=24:
                self.y = other.bottom - self.size[Y]-1
                return
            if self.gravity>= 0:
                self.y = other.bottom - self.size[Y] - 2
                self.gravity = 0
        elif group == 'yoshi:largeBlock':
            if self.cur_state == HITTING and self.hitting_time<=24:
                self.y = other.pos.bottom - self.size[Y]-1
                return
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
            if self.cur_state == HITTING and self.hitting_time<=24:
                self.y = other.pos.bottom - self.size[Y]-1
                return
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
                    other.play_bgm()

        elif group == 'yoshi:finishLine':
            if self.state == "MARIO":
                self.cur_state = WALK
                game_framework.push_state(finish_state)
        elif group == 'yoshi:enemies':
            if self.cur_state==HITTING: return
            if other.grabbed: return
            if self.state == "MARIO":
                self.state = "NOMARIO"
                play_state.babyMario = item.BabyMario(self.x-170,self.y+150)
                play_state.spawnMario = True
                play_state.game_over_timer_ui.start_setting()
            self.cur_state.exit(self)
            self.cur_state = HITTING
            self.cur_state.enter(self, GETHIT)
        elif group == 'yoshi:babyMario':
            play_state.yoshi.state='MARIO'
            game_world.remove_object(other)





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