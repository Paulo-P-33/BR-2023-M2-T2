import pygame
import random 

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager: 
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        value = random.randint(0, 2)
        if len(self.obstacles) == 0:
            obstacle_dic = {0: Cactus(SMALL_CACTUS, 325), 1: Cactus(LARGE_CACTUS, 300), 2: Bird(BIRD)}
            self.obstacles.append(obstacle_dic[value])
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.type == "hammer": 
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []