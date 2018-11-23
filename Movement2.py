import pygame
 
FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = 1
LEFT = 2
STOP = 3
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
x = W // 2
y = H // 2
r = 50
 
motion = STOP

while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
 
    clock.tick(FPS)