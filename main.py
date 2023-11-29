import pygame
from Background import Background
from Fish import Fish
from OrangeKrill import OrangeKrill
from PurpleKrill import PurpleKrill
from Shark import Shark
from ScoreBoard import ScoreBoard

pygame.init()
pygame.font.init()

bground = Background('Background.png', [0,0])
all_sprites = pygame.sprite.Group()
krill_sprites = pygame.sprite.Group()

fish = Fish()
orange_krill = OrangeKrill()
purple_krill = PurpleKrill()
shark = Shark()
score = ScoreBoard(30, 30, 0)

all_sprites.add(fish)
all_sprites.add(orange_krill)
all_sprites.add(purple_krill)
all_sprites.add(shark)
all_sprites.add(score)
krill_sprites.add(orange_krill)
krill_sprites.add(purple_krill)


screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 30)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
click = False
    
def main_menu():
    while True:
        screen.blit(bground.image, bground.rect)
        draw_text("Main Menu", font, (255, 255, 255), screen, 175, 50)
        
        mx, my = pygame.mouse.get_pos()
       
        text1 = font.render("Play", True, (0,0,0), (255,255,255))
        button_1 = text1.get_rect()
        button_1.center = (250, 250)
        text2 = font.render("Quit!", True, (0,0,0), (255,255,255))
        button_2 = text2.get_rect()
        button_2.center = (250, 350)
        
        
        
        if button_1.collidepoint(mx,my):
            if click:
                for entity in all_sprites:
                    entity.reset()
                game()
        if button_2.collidepoint(mx,my):
            if click:
                pygame.quit()
        screen.blit(text1, button_1)
        screen.blit(text2, button_2)
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        clock.tick(60)
        
def game():
    running = True
    while running:
        screen.blit(bground.image, bground.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    fish.left()
                elif event.key == pygame.K_RIGHT:
                    fish.right()
                elif event.key == pygame.K_UP:
                    fish.up()
                elif event.key == pygame.K_DOWN:
                    fish.down()
        for entity in all_sprites:
            entity.move()
            entity.render(screen)
        krill = pygame.sprite.spritecollideany(fish, krill_sprites)
        if krill:
            score.update(1)
            orange_krill.dx = orange_krill.dx + 0.1
            purple_krill.dy = purple_krill.dy + 0.1
            krill.reset()
        if pygame.sprite.collide_rect(fish, shark):
            running = False
        pygame.display.flip()
        clock.tick(60)
        
main_menu()