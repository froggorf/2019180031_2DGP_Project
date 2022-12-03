from pico2d import *
import random
import play_state
import game_world
LEFT = 0
RIGHT = 1
X = 0
Y = 1
class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 2
        self.frame = 0
        self.movetime = 0
        self.waittime = random.randint(30,100)
        self.face = LEFT
        self.grabbed = False
        self.can_attack = True
    # def draw(self):
    #     pass

    def update(self):
        pass



class Rocket(Enemy):
    image = None
    def __init__(self,s_x,s_y,e_x= 0,e_y=None):

        super(Rocket, self).__init__(random.randint(0,6000),s_y)
        if Rocket.image == None:
            Rocket.image = load_image('resource\\enemies\\enemy.png')
        self.size = [int(146/5*3), int(132/5*3)]
        self.startx = s_x
        self.starty = s_y
        self.endx = e_x
        self.endy = e_y
        self.speed = random.randint(3,10)
        self.can_attack=False
    def draw(self,left, bottom, right, top):
        Rocket.image.clip_draw(146*int(self.frame), 1000-97-132, 146, 132,
                               self.x - left + self.size[X] // 2, self.y - bottom + self.size[Y] // 2, self.size[X], self.size[Y])



    def update(self):
        self.frame=(self.frame+0.2)%2
        self.move()

    def move(self):
        self.x -= self.speed
        if self.x <= self.endx:
            self.x = self.startx
    def get_bb(self):
        return self.x, self.y, self.x + self.size[X], self.y + self.size[Y]

    def handle_collision(self, other, group):
        if self == other: return






class Flower(Enemy):
    image = None
    def __init__(self,x,y):
        super(Flower, self).__init__(x,y)
        if Flower.image == None:
            Flower.image = load_image('resource\\enemies\\enemy.png')
        self.size = [61,85]

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
        if self.grabbed: return
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
        for rect in play_state.groundRect:
            if play_state.collide(self,rect):
                if self.face == LEFT:
                    self.x = rect.right+1
                else:
                    self.x = rect.left-self.size[X] -1
        for rect in play_state.largeBlock:
            if play_state.collide(self,rect):
                if self.face == LEFT:
                    self.x = rect.pos.right+1
                else:
                    self.x = rect.pos.left - self.size[X] - 1
        for rect in play_state.footBlock:
            if play_state.collide(self,rect):
                if self.face == LEFT:
                    self.x = rect.pos.right+1
                else:
                    self.x = rect.pos.left - self.size[X] - 1
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        pass

    def calc_gravity(self):
        self.y -= 5
        # self.check_ground()



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


    def get_bb(self):
        return self.x, self.y, self.x + 61, self.y + 85

    def handle_collision(self, other, group):
        if self == other: return
        #print('enemies 가 무언가랑 만났다고 함')
        if group == 'tongue:enemies':
            self.grabbed = True
            if other.tongue_length <= 20:
                other.eatting += 1
                game_world.remove_object(self)
                play_state.enemies.remove(self)
            if other.face == RIGHT:
                self.x = other.x+30+other.tongue_length-10
                self.y = other.y
            else:
                self.x = other.x+25-other.tongue_length+5
                self.y=other.y


        if self.grabbed : return
        if group == 'enemies:groundRect':
            self.y = other.top + 1
        elif group == 'enemies:stairRect':
            self.y = other.top + 1
        elif group == 'enemies:ceilingBlock':
            self.y = other.bottom - 85 - 2
        elif group == 'enemies:largeBlock':
            self.y = other.pos.top + 1
        elif group == 'yoshi:footBlock':
            self.y = other.pos.top + 1



