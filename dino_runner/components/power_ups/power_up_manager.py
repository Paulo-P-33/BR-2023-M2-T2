import random 
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        self.power_up_type = [
            Shield(),
            Hammer(),
            Heart(),
        ]

        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(self.power_up_type[random.randint(0, len(self.power_up_type) - 1)])

    def update(self, score, game, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                #player settings
                if power_up.type == "heart":
                    game.heart_count += 1
                else:
                    player.has_power_up = True
                    player.type = power_up.type
                    player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
        

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)