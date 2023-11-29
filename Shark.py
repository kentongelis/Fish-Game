import pygame
from GameObj import GameObject
import random

class Shark(GameObject):
    def __init__(self):
        super(Shark, self).__init__(0,0, 'shark.png')
        self.surf = pygame.transform.scale(self.surf, (100,100))
        self.dx = 0
        self.dy = 0
        self.reset()
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 564 and self.dx > 0:
            self.surf = pygame.image.load('shark.png')
            self.surf = pygame.transform.scale(self.surf, (100,100))
            self.reset()
        elif self.x < -64 and self.dx < 0:
            self.surf = pygame.image.load('shark.png')
            self.surf = pygame.transform.scale(self.surf, (100,100))
            self.reset()        
        elif self.y > 564 and self.dy > 0:
            self.surf = pygame.image.load('shark.png')
            self.surf = pygame.transform.scale(self.surf, (100,100))
            self.reset()
        elif self.y < -64 and self.dy < 0:
            self.surf = pygame.image.load('shark.png')
            self.surf = pygame.transform.scale(self.surf, (100,100))
            self.reset()

    def reset(self):
        self.surf = pygame.image.load('shark.png')
        self.surf = pygame.transform.scale(self.surf, (100,100))
        start = [93,218,343]
        numbs = [0,1,2,3]
        num = random.choice(numbs)
        if num == 0:
            self.dx = 5
            self.dy = 0
            self.x = -64
            self.y = random.choice(start)
        elif num == 1:
            self.dx = -5
            self.dy = 0
            self.x = 564
            self.y = random.choice(start)
            self.surf = pygame.transform.flip(self.surf, True, False)
        elif num == 2:
            self.dx = 0
            self.dy = 5
            self.x = random.choice(start)
            self.y = -64
            self.surf = pygame.transform.rotate(self.surf, 270)
        elif num == 3:
            self.dx = 0 
            self.dy = -5
            self.x = random.choice(start)
            self.y = 564
            self.surf = pygame.transform.rotate(self.surf, 90)