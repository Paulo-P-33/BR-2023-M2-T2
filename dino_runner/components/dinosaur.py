import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import *

DUCK_IMG = {DEFAULT_TYPE: DUCKING, POWER_UP_TYPE["shield"]: DUCKING_SHIELD, POWER_UP_TYPE["hammer"]: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, POWER_UP_TYPE["shield"]: JUMPING_SHIELD, POWER_UP_TYPE["hammer"]: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, POWER_UP_TYPE["shield"]: RUNNING_SHIELD, POWER_UP_TYPE["hammer"]: RUNNING_HAMMER}

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.power_up = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
        
        

        if self.step_index >= 9:
            self.step_index = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = 340
        self.step_index += 1
        self.dino_duck = False