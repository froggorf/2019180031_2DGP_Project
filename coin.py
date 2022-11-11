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



import stage
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

    def update(self, l,b,r,t):
        Coin.frame = (Coin.frame+0.01) % 4
        temp = stage.myRect(l,b,r,t)
        if self.myIntersectRect(temp):
            return 100


    # TODO: 나중에 game_World에 넣고서 충돌체크 리팩토링 하고선 지우기
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