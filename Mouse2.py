import pygame

STATEBLUE = (106, 90, 205)
LAVENDERBLUSH = (255, 240, 245)
ROYALBLUE = (65, 105, 225)
LIGHTSLATEBLUE = (132, 112, 255)

FPS = 120
Screen_H = 600
Screen_W = 600
i = 0

pygame.init()
surface = pygame.display.set_mode((Screen_W, Screen_H))
#clock = pygame.time.Clock()

surface.fill(STATEBLUE)

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if pressed[0]:
        pygame.draw.circle(surface, LAVENDERBLUSH, pos, 50)
        pygame.display.update()
 
    pygame.time.delay(20)