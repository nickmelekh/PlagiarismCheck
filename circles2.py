import pygame
import random
 
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 20)
BLACK = (0, 0, 0)

win_width = 1280
win_height = 700

active = False

circles = []
n = 25

class Round:

    def __init__(self, surface, color, position, radius):
        self.radius = radius
        self.surface = surface
        self.color = color
        #self.x = surface.get_width() // 2
        #self.y = surface.get_height() // 2
        self.pos = position

    def expand(self, delta):
        if self.radius <= 200:
            pygame.draw.circle(self.surface, RED, self.pos, self.radius + 9)
            pygame.draw.circle(self.surface, BLUE, self.pos, self.radius + 6)
            pygame.draw.circle(self.surface, BLACK, self.pos, self.radius + 3)
            pygame.draw.circle(self.surface, self.color, self.pos, self.radius)
            self.radius += random.randint(0, 6)
        else:
            self.radius = 1
            pygame.draw.circle(self.surface, GREEN, self.pos, self.radius + 3)
            pygame.draw.circle(self.surface, self.color, self.pos, self.radius)
            self.pos = (random.randint(0, win_width), random.randint(0, win_height))

pygame.init()
sc = pygame.display.set_mode((win_width, win_height))

surf = pygame.Surface((win_width, win_height))

for i in range(n):
    circles.append(Round(surf, WHITE, (random.randint(0, win_width), random.randint(0, win_height)), random.randint(0, 30)))

while 1:

    surf.fill(WHITE)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()  
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                active = True
            elif i.button == 3:
                active = False
                
    if active == True:
        for circle in circles:
            circle.expand(random.randint(0, 10))
        sc.blit(surf, (0, 0))
        print(len(circles))

        pygame.display.update()

    pygame.time.delay(10)

