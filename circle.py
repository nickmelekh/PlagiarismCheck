import pygame
import random
 
FPS = 60
WIN_WIDTH = 1280
WIN_HEIGHT = 600
speed_up = 3
n = 30
i = 0
 
WHITE = (255, 255, 255)
LIGHT_BLUE = (64, 128, 255)
BLACK = (0, 0, 0)
#RANDOM = random.randint(0, 255) 
 
pygame.init()
 
clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
#sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

Length = 30
x = []
x1 = 0
for i in range(n):
    x1 += 15
    x.append(x1)
y = 0
 
while 1:
    sc.fill(BLACK)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
    
    for i in range(n):
        pygame.draw.rect(sc, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x[i], y, Length, WIN_HEIGHT))
 
    pygame.display.update()

    for i in range(n):
        if x[i] >= WIN_WIDTH + Length:
            x[i] = 0 - Length
        else:
            speed_up = i * 0.1
            x[i] += speed_up
 
    clock.tick(FPS)