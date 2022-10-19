from pico2d import *
import yoshi_character
X = 0
Y = 1




class StageState:
    def __init__(self):
        #카메라(화면출력) 관련
        self.cameraPos = [0,0]
        #from main import width, height
        self.cameraSize = [1200,975]
        self.dir = [0,0]
        self.cameraSpeed = 5

        #이미지 관련
        self.image = [load_image("stage1_1.png")]

        #스테이지 구분 관련
        self.selectStage = 0

        #스테이지마다 다르게 갖는 변수
        self.groundRect = [
            myRect(0,0,832,512),
            myRect(1024,0,1536,512),
            myRect(1680,608,1820,650),
            myRect(1820,0,2368,608),
            myRect(2371,0,2373,837)
        ]
        self.stairRect = [
            myRect(830,0,880,528),
            myRect(864,0,896,560),
            myRect(896,0,928,592),
            myRect(928,0,960,560),
            myRect(1568,0,1576,592),
            myRect(1624,0,1626,688)
        ]
        self.footBlock = [
            FootBlock(1921, 3263 - 2494, 1921 + 62, 3263 - 2494 + 62, "BLOCK"),
            FootBlock(1983, 3263 - 2494, 1983 + 62, 3263 - 2494 + 62, "BLOCK"),
            FootBlock(2107, 3263 - 2494, 2107 + 62, 3263 - 2494 + 62, "BLOCK"),
            FootBlock(2169, 3263 - 2494, 2169 + 62, 3263 - 2494 + 62, "BLOCK")
        ]
        self.largerBlock = [
            FootBlock(2045, 3263 - 2494, 2045 + 62, 3263 - 2494 + 62, "LARGER_BLOCK"),
        ]

    #그리기 관련 함수
    def draw(self, yoshi_x, yoshi_y):
        self.cameraPos[X] = yoshi_x - self.cameraSize[X]//2
        self.cameraPos[Y] = yoshi_y - self.cameraSize[Y]//2
        if self.cameraPos[X] <0: self.cameraPos[X] = 0
        if self.cameraPos[Y] <0 : self.cameraPos[Y]=0
        if self.cameraPos[X]+self.cameraSize[X] > self.image[self.selectStage].w : self.cameraPos[X] = self.image[self.selectStage].w - self.cameraSize[X]
        if self.cameraPos[Y] + self.cameraSize[Y] > self.image[self.selectStage].h:self.cameraPos[Y] = self.image[self.selectStage].h - self.cameraSize[Y]
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



class FootBlock():
    def __init__(self,g_left=0,g_bottom=0, g_right=0,g_top=0, g_type = "BLOCK"):
        self.pos = myRect(g_left,g_bottom,g_right,g_top)
        self.type = g_type
        self.image = load_image('foot_block.png')
        self.largertime = 0
        self.first_w = self.pos.get_w()
        self.first_h = self.pos.get_h()
        self.larger_block = False

    def draw(self, left, bottom, right, top):
        if self.type == "BLOCK":
            self.image.clip_draw(63, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())
        elif self.type == "LARGER_BLOCK":
            self.image.clip_draw(0, 0, 63, 62, self.pos.left - left + self.pos.get_w() // 2, self.pos.bottom - bottom + self.pos.get_h() // 2, self.pos.get_w(), self.pos.get_h())

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

    def large_block(self):
        if self.larger_block:
            if self.largertime >= 19:
                self.larger_block = False
            self.pos.left-=self.first_w//20
            self.pos.right+=self.first_w//20
            self.pos.bottom+=self.first_h//20
            self.pos.top+=self.first_h//20*3
            self.largertime+=1



