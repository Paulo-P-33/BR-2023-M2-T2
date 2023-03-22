import random

from dino_runner.utils.constants import HAMMER, POWER_UP_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = POWER_UP_TYPE["hammer"]
        super().__init__(self.image, self.type)
        self.rect.y = random.choice([200, 300])
    
    