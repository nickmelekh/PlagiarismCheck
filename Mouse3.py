import pygame

STATEBLUE = (106, 90, 205)
LAVENDERBLUSH = (255, 240, 245)
ROYALBLUE = (65, 105, 225)
LIGHTSLATEBLUE = (132, 112, 255)
BLACK = (0, 0, 0)

FPS = 60
Screen_H = 600
Screen_W = 600
i = 0

pygame.init()
surface = pygame.display.set_mode((Screen_W, Screen_H))
clock = pygame.time.Clock()

surface.fill(BLACK)

while 1:

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				while i < 60:
					print(i)
					pygame.draw.circle(surface, LAVENDERBLUSH, event.pos, i)
					pygame.display.update()
					i += 1
	clock.tick(FPS)
