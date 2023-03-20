import pygame
import random 

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager: 
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        value = random.randint(0, 1)
        if len(self.obstacles) == 0:
            if value == 0:
                allCactus = SMALL_CACTUS + LARGE_CACTUS
                self.obstacles.append(Cactus(allCactus))
            elif value == 1:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)