from pico2d import *
import random

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 10
        self.frame = 0


    def draw(self):
        pass

    def update(self):
        pass


class Flower(Enemy):
    image = None
    def __init__(self,x,y):
        super(Flower, self).__init__(x,y)
        if Flower.image == None:
            Flower.image = load_image('enemy.png')

    def draw(self):
        Flower.image.clip_draw(61*int(self.frame),1000-85,61,85,self.x,self.y)
        pass

    def update(self):
        self.frame=(self.frame+0.2)%5
        pass















