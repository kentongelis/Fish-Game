import pygame
from GameObj import GameObject
from ResourcePath import resourcepath


lanes = [93, 218, 343]

fish_image = resourcepath('fish.png')

class Fish(GameObject):
    def __init__(self):
        super(Fish,self).__init__(0,0, fish_image)
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()
        
    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()
        self.surf = pygame.image.load(fish_image)
        self.surf = pygame.transform.flip(self.surf, True, False)

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()
        self.surf = pygame.image.load(fish_image)

    def up(self):
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()
        self.surf = pygame.image.load(fish_image)
        self.surf = pygame.transform.rotate(self.surf, 90)

    def down(self):
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()
        self.surf = pygame.image.load(fish_image)
        self.surf = pygame.transform.rotate(self.surf, 270)

    def move(self):
        self.x -= (self.x - self.dx) * 0.25 
        self.y -= (self.y - self.dy) * 0.25
        if self.x > 500-(32+58):
            self.x = 500-(32+58)
        if self.x < 32:
            self.x = 32
        if self.y > 500-(32+58):
            self.y = 500-(32+58)
        if self.y < 32:
            self.y = 32
    
    def reset(self):
        self.surf = pygame.image.load(fish_image)
        self.x = lanes[1]
        self.y = lanes[1]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]