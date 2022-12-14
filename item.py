import random
from pico2d import *

import game_world
import play_state

X= 0
Y= 1
LEFT = 0
RIGHT = 1

class Item:
    image = None
    def __init__(self,x,y):
        if Item.image == None:
            Item.image = load_image('resource\\item\\item.png')
        self.x = x
        self.y = y


class EventBox(Item):
    frame = None
    bgm = None
    def __init__(self, x, y,eventfunc):
        super(EventBox, self).__init__(x, y)
        self.size = [54,60]
        self.offset = [150,77]
        self.event_func = eventfunc

        if EventBox.frame == None:
            EventBox.frame = 0
        if EventBox.bgm == None:
            EventBox.bgm = load_wav('resource\\sound\\event_box.wav')
            EventBox.bgm.set_volume(50)
    def draw(self, left, bottom, right, top):
        Item.image.clip_draw(
            0,
            700 - 575-77+self.offset[Y]*int(EventBox.frame),
            self.offset[X],
            self.offset[Y],
            self.x - left + self.offset[X] // 2,
            self.y - bottom + self.offset[Y] // 2,
            self.offset[X],
            self.offset[Y]
        )

    def update(self):
        EventBox.frame = (EventBox.frame+0.07)%4
        pass
        # Coin.frame = (Coin.frame + 0.01) % 4
        # # from stage import myRect
        # # temp = myRect(l,b,r,t)
        # # if self.myIntersectRect(temp):
        # #     return 100

    def get_bb(self):
        mid_x = self.x + self.offset[X]//2
        mid_y = self.y + self.offset[Y]//2
        return mid_x-self.size[X]//2,mid_y-self.size[Y]//2,mid_x+self.size[X]//2,mid_y+self.size[Y]//2

    def handle_collision(self, other, group):
        if group == 'eggs:eventbox':
            EventBox.bgm.play(1)
            self.event_func()
            game_world.remove_object(self)
            if self in play_state.eventbox:
                play_state.eventbox.remove(self)


class Egg(Item):

    def __init__(self, x, y, radian,face):
        super(Egg, self).__init__(x,y)
        self.radian = radian
        self.size = [84//3*2,90//3*2]
        self.speed = 15
        self.face = face

    def draw(self, left, bottom, right, top):
        Item.image.clip_draw(
            0,
            700 - 333,
            84,
            90,
            self.x - left + 84//2,
            self.y - bottom + 90// 2,
            self.size[X],
            self.size[Y]
        )

    def update(self):
        if self.face == RIGHT:
            self.x += self.speed
        else:
            self.x -= self.speed
        self.y+=self.radian * self.speed
        pass

    def get_bb(self):
        return self.x, self.y+15, self.x + self.size[X], self.y + self.size[Y]

    def handle_collision(self, other, group):
        if self==other: return
        if group == 'eggs:enemies':
            game_world.remove_object(other)
            if other in play_state.enemies:
                play_state.enemies.remove(other)
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:groundRect':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:stairRect':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:ceilingBlock':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:footBlock':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:largeBlock':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)
        elif group == 'eggs:eventbox':
            game_world.remove_object(self)
            if self in play_state.eggs:
                play_state.eggs.remove(self)





class Coin(Item):
    frame = None
    bgm = None
    def __init__(self,x,y):
        super(Coin, self).__init__(x,y)
        self.size = [45,60]


        if Coin.frame == None:
            Coin.frame = 0
        if Coin.bgm ==None:
            Coin.bgm = load_wav('resource\\sound\\coin.wav')
            Coin.bgm.set_volume(32)

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
        if group == 'eggs:coins':
            Coin.bgm.play(1)
            play_state.stageState.coin_num+=1
            game_world.remove_object(self)
            if self in play_state.coins:
                play_state.coins.remove(self)
        elif group == 'yoshi:coins':
            Coin.bgm.play(1)
            play_state.stageState.coin_num+=1
            game_world.remove_object(self)
            if self in play_state.coins:
                play_state.coins.remove(self)

LEFT = 0
RIGHT = 1
class BabyMario(Item):
    frame = None

    def __init__(self,x,y):
        super(BabyMario, self).__init__(x,y)
        if BabyMario.frame == None:
            BabyMario.frame = 0

        self.bgm = load_wav('resource\\sound\\baby_mario_cry.wav')
        self.bgm.play(1)
        self.bgm.set_volume(20)
        self.bgm_time = 0

        self.size = [81,81]
        self.gravity = 0
        self.face = LEFT
        self.up = False

    def update(self):
        BabyMario.frame = (BabyMario.frame+0.1)%2
        self.bgm_time += (1/60)
        if self.bgm_time >= 0.5:
            self.bgm_time = 0
            self.bgm.play(1)




        if self.face == LEFT:
            self.x-=1
            if self.x<0:
                self.x = 0
        else:
            self.x +=1
        for rect in play_state.groundRect:
            if play_state.collide(self, rect):
                if self.face == LEFT:
                    self.x = rect.right + 3
                else:
                    self.x = rect.left - self.size[X] - 1
        for rect in play_state.largeBlock:
            if play_state.collide(self, rect):
                if self.face == LEFT:
                    self.x = rect.pos.right + 1
                else:
                    self.x = rect.pos.left - self.size[X] - 1
        for rect in play_state.footBlock:
            if play_state.collide(self, rect):
                if self.face == LEFT:
                    self.x = rect.pos.right + 1
                else:
                    self.x = rect.pos.left - self.size[X] - 1

        self.y += self.gravity

        if self.up:
            self.gravity -= 0.5
            if self.gravity == -10:
                self.up = False
        else:
            self.gravity += 0.5
            if self.gravity == 10:
                self.up = True
                if random.randint(0, 4) == 0:
                    if self.face == LEFT:
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
        if group == 'babyMario:groundRect':
            if self.gravity >= 0:
                self.y = other.bottom - self.size[Y] - 1
            else:
                self.y = other.top + 1
        elif group == 'babyMario:stairRect':
            if self.gravity>=0:
                self.y = other.bottom - self.size[Y]-1
            else:
                self.y = other.top + 1
        elif group == 'babyMario:ceilingBlock':
            if self.gravity >= 0:
                self.y = other.bottom - self.size[Y] - 2
        elif group == 'babyMario:largeBlock':
            if self.gravity >= 0:
                self.y = other.pos.bottom - self.size[Y] - 1
            else:
                self.y = other.pos.top + 1
        elif group == 'babyMarioW:footBlock':
            if self.gravity >= 0:
                self.y = other.pos.bottom - self.size[Y] - 1
            else:
                self.y = other.pos.top + 1



