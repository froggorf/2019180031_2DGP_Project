from pico2d import *
import yoshi_character
import stage_select_state
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
        self.image = [load_image("stage1_1.png")]
        self.background_image = [load_image("stage1_background.png")]

        #스테이지 구분 관련
        self.selectStage = stage_select_state.select_stage


        #TODO: 스테이지마다 다르게 갖도록
        #맵 충돌체크 관련 변수들은 게임월드를 통한 관리 or 깔끔한 처리를 위한 리팩토링 진행 예정
        self.groundRect = [
            myRect(0,0,832,512),
            myRect(1024,0,1536,512),
            myRect(1680,608,1820,650),
            myRect(1820,0,2368,608),
            myRect(2371,0,2373,837),
            myRect(3010,700,3015,1000),
            myRect(2880,940,3000,1100),
            myRect(3000,1060,3340,1080),
            myRect(3253,0,4044,530),
            myRect(3250,0,3253,998),
            myRect(3270,980,3385,1045),
            myRect(4042,0,4045,1150),
            myRect(3905,1272,3910,1345),
            myRect(4080,1282,4308,1334),
            myRect(4290,1219,4798,1274),
            myRect(4749,1284,4755,1420),
            myRect(4544,1600,4570,1727),
            myRect(4787,1693,5307,1728),
            myRect(5121,2735,5188,2890),
            myRect(5260,1729,5317,2680),
            myRect(5333,3262-404,6142,3262-381)
        ]
        self.stairRect = [
            myRect(830,0,880,528),
            myRect(864,0,896,560),
            myRect(896,0,928,592),
            myRect(928,0,960,560),
            myRect(1568,0,1576,592),
            myRect(1624,0,1626,688),
            myRect(2450,0,2450,907),
            myRect(2510,0,2564,950),
            myRect(2606,0,2608,900),
            myRect(2646,0,2648,850),
            myRect(2688,0,2690,800),
            myRect(2690,0,2850,770),
            myRect(2850,0,2950,735),
            myRect(2995,1130,3005,1150),
            myRect(2950,1120,3050, 1130),
            myRect(3976,1347,3990,1402),
            myRect(4028,1352,4035,1445),
            myRect(4066,1347,4090,1402),
            myRect(4634,1685,4723,1780),
            myRect(5204,3262-392,5299,3262-343)
        ]
        self.ceilingBlock = [
            myRect(2960,870,3000,1100),
            myRect(2880,920,3000,1100),
            myRect(3904, 1200, 4020, 1300),
            myRect(4020,1150,4100,1250),
            myRect(4708,1419,4767,1503),
            myRect(4647,1466,4705,1551),
            myRect(4589,1532,4647,1614),
            myRect(4552,1673,4609,1590),
            myRect(5136,2660,5256,2783)
        ]
        self.footBlock = [
            FootBlock(1921, 3263 - 2494, 1921 + 62, 3263 - 2494 + 62),
            FootBlock(1983, 3263 - 2494, 1983 + 62, 3263 - 2494 + 62),
            FootBlock(2107, 3263 - 2494, 2107 + 62, 3263 - 2494 + 62),
            FootBlock(2169, 3263 - 2494, 2169 + 62, 3263 - 2494 + 62),
            FootBlock(3460, 3263 - 2558, 3460+62, 3263-2558+62),
            FootBlock(3522, 3263 - 2558, 3522+62, 3263-2558+62),
            FootBlock(3646, 3263 - 2558, 3646+62, 3263-2558+62),
            FootBlock(3708, 3263 - 2558, 3708+62, 3263-2558+62),
        ]
        self.largerBlock = [
            LargeBlock(2045, 3263 - 2494, 2045 + 62, 3263 - 2494 + 62),
            LargeBlock(3584,3263-2558,3584+62,3263-2558+62)
        ]
        self.jumpBlock =[
            JumpBlock(500,508,500+62,508+62,101),
            JumpBlock(4432,1275,4432+62,1275+62,75),
            JumpBlock(4994,1720,4994+62,1720+62,115)
        ]

        self.finishLine = myRect(5747,2870,6139,3262)
    #그리기 관련 함수
    def draw(self, yoshi_x, yoshi_y):
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
        #foot_block 출력
        for rect in self.footBlock:
            if rect.myIntersectRect(self.cameraPos[X],self.cameraPos[Y],self.cameraPos[X]+self.cameraSize[X],self.cameraPos[Y]+self.cameraSize[Y]):
                rect.draw(self.cameraPos[X],self.cameraPos[Y],self.cameraPos[X]+self.cameraSize[X],self.cameraPos[Y]+self.cameraSize[Y])
        for rect in self.largerBlock:
            if rect.myIntersectRect(self.cameraPos[X],self.cameraPos[Y],self.cameraPos[X]+self.cameraSize[X],self.cameraPos[Y]+self.cameraSize[Y]):
                rect.draw(self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X] + self.cameraSize[X],self.cameraPos[Y] + self.cameraSize[Y])
        for rect in self.jumpBlock:
            if rect.myIntersectRect(self.cameraPos[X],self.cameraPos[Y],self.cameraPos[X]+self.cameraSize[X],self.cameraPos[Y]+self.cameraSize[Y]):
                rect.draw(self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X] + self.cameraSize[X],self.cameraPos[Y] + self.cameraSize[Y])

        #충돌체크 사각형 출력
        # for rect in self.groundRect:
        #     if rect.myIntersectRect(self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X] + self.cameraSize[X],self.cameraPos[Y] + self.cameraSize[Y]):
        #         draw_rectangle(rect.left-self.cameraPos[X],rect.bottom-self.cameraPos[Y],rect.left-self.cameraPos[X]+rect.get_w(),rect.bottom-self.cameraPos[Y]+rect.get_h())
        #
        # for rect in self.stairRect:
        #     if rect.myIntersectRect(self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X] + self.cameraSize[X],self.cameraPos[Y] + self.cameraSize[Y]):
        #         draw_rectangle(rect.left - self.cameraPos[X], rect.bottom - self.cameraPos[Y],rect.left - self.cameraPos[X] + rect.get_w(),rect.bottom - self.cameraPos[Y] + rect.get_h())
        #
        # for rect in self.ceilingBlock:
        #     if rect.myIntersectRect(self.cameraPos[X], self.cameraPos[Y], self.cameraPos[X] + self.cameraSize[X],self.cameraPos[Y] + self.cameraSize[Y]):
        #         draw_rectangle(rect.left - self.cameraPos[X], rect.bottom - self.cameraPos[Y],rect.left - self.cameraPos[X] + rect.get_w(),rect.bottom - self.cameraPos[Y] + rect.get_h())


    #업데이트
    def update(self):
        self.check_larger_block()
        pass

    def cameraMove(self):
        self.cameraPos[X] += self.dir[X]*self.cameraSpeed
        self.cameraPos[Y] += self.dir[Y]*self.cameraSpeed
        if self.cameraPos[X] < 0: self.cameraPos[X] = 0
        if self.cameraPos[Y] < 0: self.cameraPos[Y] = 0
        if self.cameraPos[X] + self.cameraSize[X] > self.image[self.selectStage].w: self.cameraPos[X] = self.image[self.selectStage].w - self.cameraSize[X]
        if self.cameraPos[Y] + self.cameraSize[Y] > self.image[self.selectStage].h: self.cameraPos[Y] = self.image[self.selectStage].h - self.cameraSize[Y]

    def check_larger_block(self):
        for rect in self.largerBlock:
            rect.large_block()



class myRect:
    def __init__(self, g_left=0, g_bottom=0, g_right=0, g_top=0):
        self.left = g_left
        self.bottom = g_bottom
        self.right = g_right
        self.top = g_top


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



class FootBlock():
    image = None
    def __init__(self,g_left=0,g_bottom=0, g_right=0,g_top=0):
        self.pos = myRect(g_left,g_bottom,g_right,g_top)
        if FootBlock.image==None:
            FootBlock.image = load_image('foot_block.png')

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(63, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())


    def myIntersectRect(self, left, bottom, right, top):
        if left == -1: return
        bVertical = False
        bHorizontal = False

        if self.pos.left < right and self.pos.right > left:
            bHorizontal = True

        if self.pos.top > bottom and self.pos.bottom < top:
            bVertical = True

        if bVertical and bHorizontal:
            return True
        else:
            return False



class LargeBlock(FootBlock):
    image = None
    def __init__(self,g_left,g_bottom,g_right,g_top):
        self.pos = myRect(g_left, g_bottom, g_right, g_top)
        if LargeBlock.image==None:
            LargeBlock.image = load_image('foot_block.png')
        self.largertime = 0
        self.first_w = self.pos.get_w()
        self.first_h = self.pos.get_h()
        self.larger_block = False

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(0, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())

    def large_block(self):
        if self.larger_block:
            if self.largertime >= 19:
                self.larger_block = False
            self.pos.left-=self.first_w//40
            self.pos.right+=self.first_w//40
            self.pos.bottom+=self.first_h//19
            self.pos.top+=self.first_h//12
            self.largertime+=1

class JumpBlock(FootBlock):
    image = None
    def __init__(self, g_left=0, g_bottom=0, g_right=0, g_top=0, jumppower=0):
        self.pos = myRect(g_left, g_bottom, g_right, g_top)
        if JumpBlock.image == None:
            JumpBlock.image = load_image('foot_block.png')
        self.jump_power = jumppower

    def draw(self, left, bottom, right, top):
        self.image.clip_draw(126, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2,
                             self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())
