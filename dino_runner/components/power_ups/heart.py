import random

from dino_runner.utils.constants import HEART, POWER_UP_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Heart(PowerUp):
    def __init__(self):
        self.image = HEART
        self.type = POWER_UP_TYPE["heart"]
        super().__init__(self.image, self.type)
        self.rect.y = 350 #random.choice([200, 300])
    
    