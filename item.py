import random
from pico2d import *
X= 0
Y= 1

class Item:
    image = None
    def __init__(self,x,y):
        if Item.image == None:
            Item.image = load_image('item.png')
        self.x = x
        self.y = y


class Coin(Item):
    frame = None
    def __init__(self,x,y):
        super(Coin, self).__init__(x,y)
        self.size = [45,60]


        if Coin.frame == None:
            Coin.frame = 0

    def draw(self,left,bottom,right,top):
        Item.image.clip_draw(
            60*int(Coin.frame),
            700-80,
            60,
            80,
            self.x - left + self.size[X] // 2,
            self.y - bottom + self.size[Y] // 2,
            self.size[X],
            self.size[Y]
        )

    def update(self):
        Coin.frame = (Coin.frame+0.01) % 4
        # from stage import myRect
        # temp = myRect(l,b,r,t)
        # if self.myIntersectRect(temp):
        #     return 100



    def get_bb(self):
        return self.x, self.y, self.x + self.size[X], self.y + self.size[Y]

    def handle_collision(self, other, group):
        print('coin 가 무언가랑 만났다고 함')


LEFT = 0
RIGHT = 1
class BabyMario(Item):
    frame = None
    def __init__(self,x,y):
        super(BabyMario, self).__init__(x,y)
        if BabyMario.frame == None:
            BabyMario.frame = 0
        self.size = [81,81]
        self.gravity = 0
        self.face = LEFT
        self.up = False

    def update(self):
        BabyMario.frame = (BabyMario.frame+0.1)%2
        if self.face == LEFT:
            self.x-=1
        else:
            self.x +=1
        self.y += self.gravity
        if self.up:
            self.gravity -= 0.5
            if self.gravity == -10 :
                self.up = False
        else:
            self.gravity += 0.5
            if self.gravity == 10:
                self.up=True
                if random.randint(0,4)==0:
                    if self.face ==LEFT:
                        self.face = RIGHT
                    else:
                        self.face = LEFT




    def draw(self,left,bottom,right,top):
        Item.image.clip_draw(
            162*int(BabyMario.frame),
            700-80-162,
            162,
            162,
            self.x - left + self.size[X] // 2,
            self.y - bottom + self.size[Y] // 2,
            self.size[X],
            self.size[Y]
        )


    def get_bb(self):
        return self.x, self.y, self.x + self.size[X], self.y + self.size[Y]

    def handle_collision(self, other, group):
        print('babyMario 가 무언가랑 만났다고 함')
