
import pygame, sys, math, random
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

r1t = pygame.image.load("Road\hTop.png")
r1tr = r1t.get_rect(topleft = [75,50])
r1m = pygame.image.load("Road\middle.png")
r1mr = r1m.get_rect(topleft = [75,75])
r1b = pygame.image.load("Road\hBottom.png")
r1br = r1b.get_rect(topleft = [75,100])
r2t = pygame.image.load("Road\hTop.png")
r2tr = r2t.get_rect(topleft = [100,50])
r2m = pygame.image.load("Road\middle.png")
r2mr = r2m.get_rect(topleft = [100,75])
r2b = pygame.image.load("Road\hBottom.png")
r2br = r2b.get_rect(topleft = [100,100])



bgColor = [r, g, b] = [10, 205, 73]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
    screen.fill(bgColor)
    screen.blit(r1t, r1tr)
    screen.blit(r1m, r1mr)
    screen.blit(r1b, r1br)
    screen.blit(r2t, r2tr)
    screen.blit(r2m, r2mr)
    screen.blit(r2b, r2br)
    pygame.display.flip()
    clock.tick(60)
