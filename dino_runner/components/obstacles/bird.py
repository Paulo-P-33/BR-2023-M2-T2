import random 

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.positionBird = [250, 300]
        self.type = random.randint(0, (len(image) - 1))
        super().__init__(image, self.type)
        self.rect.y = self.positionBird[random.randint(0, (len(self.positionBird) - 1))]
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 10:
            self.index = 0

        if self.index < 5:
            screen.blit(self.image[0], self.rect)
        else: 
            screen.blit(self.image[1], self.rect)
        
        self.index += 1