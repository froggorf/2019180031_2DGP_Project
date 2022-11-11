from pico2d import *
import random

LEFT = 0
RIGHT = 1
class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 2
        self.frame = 0
        self.movetime = 0
        self.waittime = random.randint(30,100)
        self.face = LEFT
    # def draw(self):
    #     pass

    def update(self):
        pass



class Flower(Enemy):
    image = None
    def __init__(self,x,y):
        super(Flower, self).__init__(x,y)
        if Flower.image == None:
            Flower.image = load_image('enemy.png')

    def draw(self,left, bottom, right, top):
        #Flower.image.clip_draw(61*int(self.frame),1000-85,61,85,self.x,self.y)
        if self.face == RIGHT:
            self.image.clip_draw(61*int(self.frame), 1000-85, 61, 85, self.x - left + 61 // 2,
                                 self.y - bottom + 85 // 2, 61, 85)
        else:
            self.image.clip_composite_draw(61*int(self.frame), 1000-85, 61, 85,0,'h', self.x - left + 61 // 2,
                                 self.y - bottom + 85 // 2, 61, 85)
        pass

    def update(self):
        self.frame=(self.frame+0.2)%5
        self.move()
        self.calc_gravity()

    def move(self):
        if self.movetime == 0:
            if self.waittime == 0:
                self.movetime = random.randint(60,120)
                self.face = RIGHT
                if random.randint(0,1)==0:
                    self.movetime*=-1
                    self.face= LEFT
            else:
                self.waittime-=1
        elif self.movetime<0:
            self.x -= self.speed
            self.movetime +=1
            if self.movetime >= 0:
                self.waittime = random.randint(60,120)
        else:
            self.x += self.speed
            self.movetime-=1
            if self.movetime <= 0:
                self.waittime = random.randint(60,120)

        self.check_block()

    def check_block(self):
        from play_state import stageState
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                if self.movetime >= 0:
                    self.x = rect.left - 70
                elif self.movetime <= 0:
                    self.x = rect.right
        for rect in stageState.largerBlock:
            if self.myIntersectRect(rect.pos):
                if self.movetime >= 0:
                    self.x = rect.left - 70
                elif self.movetime <= 0:
                    self.x = rect.pos.right
        for rect in stageState.footBlock:
            if self.myIntersectRect(rect.pos):
                if self.movetime >= 0:
                    self.x = rect.left - 70
                elif self.movetime <= 0:
                    self.x = rect.pos.right
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        pass

    def calc_gravity(self):
        self.y -= 5
        self.check_ground()



    def check_ground(self):
        from play_state import stageState
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
        for rect in stageState.stairRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
        for rect in stageState.largerBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.top
        for rect in stageState.footBlock:
            if self.myIntersectRect(rect.pos):
                self.y = rect.pos.top

    #TODO: 나중에 game_World에 넣고서 충돌체크 리팩토링 하고선 지우기
    def myIntersectRect(self, rect):
        if rect.left == -1: return
        bVertical = False
        bHorizontal = False

        if self.x < rect.right and self.x + 70 > rect.left:
            bHorizontal = True

        if self.y + 85 > rect.bottom and self.y < rect.top:
            bVertical = True

        if bVertical and bHorizontal:
            return True
        else:
            return False



