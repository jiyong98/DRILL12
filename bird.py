from pico2d import *
import game_world
import game_framework
import random
PIXEL_PER_METER = (10.0 / 1.0) # 10픽셀 100센치
RUN_SPEED_KMPH = 1.0 # km / Hour 속도는 1km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    image = None
    image2 = None
    right = True
    Left = False
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        if Bird.image2 == None:
            Bird.image2 = load_image('bird100x100x14L.png')
        self.velocity = 0
        self.x, self.y = 100, random.randint(100, 500)
        self.x2, self.y2 = 1600, self.y
        self.frame = 0


    def draw(self):
        if Bird.right:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        elif Bird.Left:
            self.image2.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if Bird.right:
            self.x += RUN_SPEED_PPS
        elif Bird.Left:
            self.x -= RUN_SPEED_PPS
        if self.x > 1500:
            Bird.Left = True
            Bird.right = False
        elif self.x < 0:
            Bird.Left = False
            Bird.right = True

