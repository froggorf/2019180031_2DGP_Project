from pico2d import *
import yoshi_character
import stage_select_state
from item import Coin
from item import BabyMario
import play_state
X = 0
Y = 1

class StageState:
    def __init__(self):
        #카메라(화면출력) 관련
        self.cameraPos = [0,0]
        #from main import width, height
        self.cameraSize = [get_canvas_width(),get_canvas_height()]
        self.dir = [0,0]
        self.cameraSpeed = 5

        #이미지 관련
        self.image = [load_image("resource\\about_stage\\stage1.png"),load_image('resource\\about_stage\\stage2.png'),load_image('resource\\about_stage\\stage3.png'),load_image('resource\\about_stage\\stage4.png')]
        self.background_image = [load_image("resource\\about_stage\\stage1_background.png"),load_image('resource\\about_stage\\stage1_background.png'),load_image('resource\\about_stage\\stage1_background.png'),load_image('resource\\about_stage\\stage4_background.png')]

        #스테이지 구분 관련
        self.selectStage = stage_select_state.select_stage -1
        print(self.selectStage)

        self.babymario = None

        self.coin_num = 0

    #그리기 관련 함수
    def draw(self, temp1,temp2,temp3,temp4):
        from play_state import yoshi
        yoshi_x = yoshi.x
        yoshi_y = yoshi.y
        self.cameraPos[X] = yoshi_x - self.cameraSize[X] // 2
        self.cameraPos[Y] = yoshi_y - self.cameraSize[Y] // 2
        backgroundPos_x = self.cameraPos[X] / self.image[self.selectStage].w * self.background_image[self.selectStage].w
        backgroundPos_y = self.cameraPos[Y] / self.image[self.selectStage].h * self.background_image[self.selectStage].h
        backgroundPos_x = int(backgroundPos_x)
        backgroundPos_y = int(backgroundPos_y)
        if self.cameraPos[X] < 0: self.cameraPos[X] = 0
        if self.cameraPos[Y] < 0: self.cameraPos[Y] = 0
        if self.cameraPos[X] + self.cameraSize[X] > self.image[self.selectStage].w: self.cameraPos[X] = self.image[self.selectStage].w - self.cameraSize[X]
        if self.cameraPos[Y] + self.cameraSize[Y] > self.image[self.selectStage].h: self.cameraPos[Y] = self.image[self.selectStage].h - self.cameraSize[Y]

        if backgroundPos_x < 0 : backgroundPos_x = 0
        if backgroundPos_y < 0: backgroundPos_y = 0
        if backgroundPos_x + self.cameraSize[X] > self.background_image[self.selectStage].w : backgroundPos_x = self.background_image[self.selectStage].w - self.cameraSize[X]
        if backgroundPos_y + self.cameraSize[Y] > self.background_image[self.selectStage].h: backgroundPos_y = self.background_image[self.selectStage].h - self.cameraSize[Y]

        #백그라운드 맵 그리기
        self.background_image[self.selectStage].clip_draw(
            backgroundPos_x,
            backgroundPos_y,
            self.cameraSize[X],
            self.cameraSize[Y],
            self.cameraSize[X]//2,
            self.cameraSize[Y]//2
        )



        #지형 맵 그리기

        self.image[self.selectStage].clip_draw(
            self.cameraPos[X],
            self.cameraPos[Y],
            self.cameraSize[X],
            self.cameraSize[Y],
            self.cameraSize[X]//2,
            self.cameraSize[Y]//2
        )

    #업데이트
    def update(self):
        pass
        # for coin in self.coins:
        #     if coin.update(play_state.yoshi.x,play_state.yoshi.y,play_state.yoshi.size[X]+play_state.yoshi.x,play_state.yoshi.y+play_state.yoshi.size[Y])==100:
        #         self.coins.remove(coin)
        #         self.coin_num+=1
        # if self.babymario!= None:
        #     if self.babymario.update(play_state.yoshi.x,play_state.yoshi.y,play_state.yoshi.size[X]+play_state.yoshi.x,play_state.yoshi.y+play_state.yoshi.size[Y]) == 100:
        #         play_state.yoshi.state = "MARIO"
        #         self.babymario = None

    def cameraMove(self):
        self.cameraPos[X] += self.dir[X]*self.cameraSpeed
        self.cameraPos[Y] += self.dir[Y]*self.cameraSpeed
        if self.cameraPos[X] < 0: self.cameraPos[X] = 0
        if self.cameraPos[Y] < 0: self.cameraPos[Y] = 0
        if self.cameraPos[X] + self.cameraSize[X] > self.image[self.selectStage].w: self.cameraPos[X] = self.image[self.selectStage].w - self.cameraSize[X]
        if self.cameraPos[Y] + self.cameraSize[Y] > self.image[self.selectStage].h: self.cameraPos[Y] = self.image[self.selectStage].h - self.cameraSize[Y]



    def get_camera(self):
        return self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X]+self.cameraSize[X], self.cameraPos[Y]+self.cameraSize[Y]



class myRect:
    def __init__(self, g_left=0, g_bottom=0, g_right=0, g_top=0):
        self.left = g_left
        self.bottom = g_bottom
        self.right = g_right
        self.top = g_top

    def draw(self,temp1,temp2,temp3,temp4):
        pass

    def update(self):
        pass
    def printRect(self):
        print(self.left, " ",self.right)

    def get_w(self):
        return self.right-self.left

    def get_h(self):
        return self.top - self.bottom

    #TODO: 나중에 지우기 temp 함수
    def myIntersectRect(self, left, bottom, right, top):
        if left == -1: return
        bVertical = False
        bHorizontal = False

        if self.left < right and self.right > left:
            bHorizontal = True

        if self.top > bottom and self.bottom < top:
            bVertical = True

        if bVertical and bHorizontal:
            return True
        else:
            return False

    def get_bb(self):
        return self.left, self.bottom, self.right, self.top

    def handle_collision(self, other, group):
        pass



class FootBlock():
    image = None
    def __init__(self,g_left=0,g_bottom=0, g_right=0,g_top=0):
        self.pos = myRect(g_left,g_bottom,g_right,g_top)
        if FootBlock.image==None:
            FootBlock.image = load_image('resource\\about_stage\\foot_block.png')

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(63, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())

    def update(self):
        pass
    def get_bb(self):
        return self.pos.left, self.pos.bottom, self.pos.right, self.pos.top

    def handle_collision(self, other, group):
        pass



class LargeBlock(FootBlock):
    image = None
    bgm = None
    def __init__(self,g_left,g_bottom,g_right,g_top):
        self.pos = myRect(g_left, g_bottom, g_right, g_top)
        if LargeBlock.image==None:
            LargeBlock.image = load_image('resource\\about_stage\\foot_block.png')
        self.largertime = 0
        self.first_w = self.pos.get_w()
        self.first_h = self.pos.get_h()
        self.larger_block = False
        if LargeBlock.bgm == None:
            LargeBlock.bgm = load_wav('resource\\sound\\larger_block.wav')
            LargeBlock.bgm.set_volume(20)
        self.play_sound = False

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(0, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())

    def update(self):
        self.check_larger_block()
        pass

    def check_larger_block(self):
            self.large_block()

    def large_block(self):
        if self.larger_block:
            if self.largertime >= 19:
                self.larger_block = False
            self.pos.left-=self.first_w//40
            self.pos.right+=self.first_w//40
            self.pos.bottom+=self.first_h//19
            self.pos.top+=self.first_h//12
            self.largertime+=1
            if self.play_sound == False:
                LargeBlock.bgm.play(1)
                self.play_sound=True

    def get_bb(self):
        return self.pos.left, self.pos.bottom, self.pos.right, self.pos.top

    def handle_collision(self, other, group):
        pass

class JumpBlock(FootBlock):
    image = None
    bgm = None
    def __init__(self, g_left=0, g_bottom=0, g_right=0, g_top=0, jumppower=0):
        self.pos = myRect(g_left, g_bottom, g_right, g_top)
        if JumpBlock.image == None:
            JumpBlock.image = load_image('resource\\about_stage\\foot_block.png')
        self.jump_power = jumppower
        if JumpBlock.bgm == None:
            JumpBlock.bgm = load_wav('resource\\sound\\jump_block.wav')
            JumpBlock.bgm.set_volume(72)

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(126, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2,
                             self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())

    def get_bb(self):
        return self.pos.left, self.pos.bottom, self.pos.right, self.pos.top

    def handle_collision(self, other, group):
        pass

    def play_bgm(self):
        JumpBlock.bgm.play(1)

class Lava:
    image = None
    frame = None
    def __init__(self,g_left,g_bottom,g_right,g_top):
        self.left =g_left
        self.bottom = g_bottom
        self.right = g_right
        self.top = g_top

        if Lava.image == None:
            Lava.image = load_image('resource\\about_stage\\lava.png')
        if Lava.frame ==None:
            Lava.frame = 0

    def update(self):
        self.top+=1.5
        Lava.frame = (Lava.frame+0.2)%16


    def draw(self,left,bottom,right,top):
        if int(self.top)-self.bottom >= 160:
            self.image.clip_draw(0,
                                 0,
                                 500,
                                 500,
                                 self.left - left + (self.right - self.left) // 2,
                                 self.bottom - bottom + (int(self.top-160) - self.bottom) // 2,
                                 self.right - self.left,
                                 int(self.top-160) - self.bottom)
            self.image.clip_draw(
                0,
                3252-2400-160+160*int(Lava.frame),
                1024,
                160,
                self.left-left+(self.right-self.left)//2,
                (int(self.top)-160) - bottom + (int(self.top)-(int(self.top)-160))//2,
                self.right-self.left,
                160,
            )
            pass
        else:
            self.image.clip_draw(
                0,
                3252 - 2400 + 160 * int(Lava.frame)-(int(self.top)-self.bottom),
                1024,
                int(self.top)-self.bottom,
                self.left - left + (self.right - self.left) // 2,
                self.bottom - bottom + (int(self.top) - self.bottom) // 2,
                self.right - self.left,
                self.top-self.bottom,
            )
        pass

    def get_bb(self):
        return self.left,self.bottom,self.right,int(self.top)

    def handle_collision(self,other,group):
        pass


