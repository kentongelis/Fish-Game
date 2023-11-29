import pygame
from GameObj import GameObject
import random


class PurpleKrill(GameObject):
    def __init__(self):
        super(PurpleKrill, self).__init__(0, 0, 'purple_krill.png')
        self.surf = pygame.transform.scale(self.surf, (50,50))
        self.dx = 0
        self.dy = (random.randint(0,200)/100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500:
            self.reset()

    def reset(self):
        start = [93,218,343]
        self.x = random.choice(start)
        self.y = -64