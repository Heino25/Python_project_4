import pygame, sys

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))

pygame.init() #initiate pygame
screen = pygame.display.set_mode((1280,720)) #Create display surface
clock = pygame.time.Clock() #Create clock object

spcaceship = SpaceShip("spaceship.png",640,500,10)
spcaceship_group = pygame.sprite.GroupSingle()
spcaceship_group.add(spcaceship)

while True: #Game loop
	for event in pygame.event.get(): #Check for events/ Player input
		if event.type == pygame.QUIT # Close the game
			pygame.quit()
			sys.exit()

	screen.fill((42,45,51))
	spcaceship_group.draw(screen)
	pygame.display.update() #Draw frame
	clock.tick(120) #COntrol the framerate