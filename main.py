import pygame
import random
from Background import Background
from Fish import Fish
from OrangeKrill import OrangeKrill
from PurpleKrill import PurpleKrill
from Shark import Shark
from ScoreBoard import ScoreBoard
from ResourcePath import resourcepath

pygame.init()
pygame.font.init()

pygame.display.set_caption("Fish Game V2")
icon = pygame.image.load(resourcepath('favicon.ico'))
pygame.display.set_icon(icon)

#'/Users/kentongelis/Desktop/Personal Code/Fish Game/Background.png'

bground = Background(resourcepath('Background.png'), [0,0])
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
surface = pygame.Surface((500,500), pygame.SRCALPHA)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
click = False

def get_high_score():
    outfile = open(resourcepath('scores.txt'), "r")
    file = outfile.read()
    scores = file.split(' ')
    if scores[0] == '':
        return ''
    else:
        scores.remove('')
        scores_list = list(map(int, scores))
        return str(max(scores_list))
    
def main_menu():
    while True:
        screen.blit(bground.image, bground.rect)
        screen.blit(surface, (0,0))
        draw_text("Main Menu", font, (255, 255, 255), screen, 175, 50)
        draw_text("Play", font, (255, 255, 255), screen, 220, 260)
        draw_text("Quit Game", font, (255, 255, 255), screen, 175, 330)
        draw_text("High Score:", font, (255,255,255), screen, 165, 125)
        draw_text(get_high_score(), font, (255,255,255), screen, 230, 180 )
        
        mx, my = pygame.mouse.get_pos()
       
        button_1 = pygame.draw.rect(surface, (0, 0, 0, 0), [220, 260, 55, 40])
        button_2 = pygame.draw.rect(surface, (0, 0, 0, 0), [175, 330, 150, 40])        
        
        if button_1.collidepoint(mx,my):
            if click:
                for entity in all_sprites:
                    entity.reset()
                orange_krill.dx = (random.randint(0,200)/100) + 1
                purple_krill.dy = (random.randint(0,200)/100) + 1
                game()
        if button_2.collidepoint(mx,my):
            if click:
                pygame.quit()
        
        
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_RETURN:
                    for entity in all_sprites:
                        entity.reset()
                    orange_krill.dx = (random.randint(0,200)/100) + 1
                    purple_krill.dy = (random.randint(0,200)/100) + 1
                    game()
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
            infile = open(resourcepath('scores.txt'), "a")
            infile.write(f'{str(score.score)} ')
        pygame.display.flip()
        clock.tick(60)
        
main_menu()