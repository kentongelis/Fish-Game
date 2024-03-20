import pygame
from GameObj import GameObject
import random
from ResourcePath import resourcepath

orange_krill = resourcepath('orange_krill.png')

class OrangeKrill(GameObject):
    def __init__(self):
        super(OrangeKrill, self).__init__(0,0, orange_krill)
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.surf = pygame.transform.flip(self.surf, True, False)
        self.dx = (random.randint(0,200)/100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.reset()
        self.y += self.dy

    def reset(self):
        start = [93,218,343]
        self.x = -64
        self.y = random.choice(start)