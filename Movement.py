import pygame

FPS = 60
Window_Width = 1280
Window_Height = 700
RIGHT = 'TO THE RIGHT'
LEFT = 'TO THE LEFT'
DOWN = 'DOWN'
UP = 'UP'
STOP = 'STOP'

WHITE = (255, 255, 255)
LIGHT_BLUE = (64, 128, 255)
BLACK = (0, 0, 0)

pygame.init()
surface = pygame.display.set_mode((Window_Width, Window_Height), pygame.RESIZABLE)

clock = pygame.time.Clock()

r = 40
x = 0
x = Window_Width // 2 - r
y = r
motion = STOP
dx = 5
dy = 5

while 1:
	surface.fill(WHITE)
	pygame.draw.circle(surface, LIGHT_BLUE, (x, y), r)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				motion = LEFT
			elif event.key == pygame.K_RIGHT:
				motion = RIGHT
			elif event.key == pygame.K_DOWN:
				motion = DOWN
			elif event.key == pygame.K_UP:
				motion = UP
		elif event.type == pygame.KEYUP:
			if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
				motion = STOP

	if motion == LEFT:
		x -= dx	
	elif motion == RIGHT:
		x += dx	
	elif motion == UP:
		y -= dy		
	elif motion == DOWN:
		y += dy	


	clock.tick(FPS)