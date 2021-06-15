import pygame, sys, random

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))

	def update(self):
		self.rect.center = pygame.mouse.get_pos()
		self.screen_constrain()

	def screen_constrain(self):
		if self.rect.right >= 1280:
			self.rect.right = 1280

		if self.rect.left <= 0:
			self.rect.left = 0

		if self.rect.top <= 0:
			self.rect.top = 0

		if self.rect.bottom >= 720:
			self.rect.bottom = 720

class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.x_speed = x_speed
		self.y_speed = y_speed

	def update(self):
		self.rect.centerx += self.x_speed
		self.rect.centery += self.y_speed

		if self.rect.centery >= 800:
			self.kill()

pygame.init() #initiate pygame
screen = pygame.display.set_mode((1280,720)) #Create display surface
clock = pygame.time.Clock() #Create clock object

spcaceship = SpaceShip("spaceship.png",640,500,10)
spcaceship_group = pygame.sprite.GroupSingle()
spcaceship_group.add(spcaceship)

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,250)

while True: #Game loop
	for event in pygame.event.get(): #Check for events/ Player input
		if event.type == pygame.QUIT:#Close the game
			pygame.quit()
			sys.exit()
		if event.type == METEOR_EVENT:
			meteor_path = random.choice(("Meteor1.png", "Meteor2.png", "Meteor3.png"))
			random_x_pos = random.randrange(0,1280)
			random_y_pos = random.randrange(-500,-50)
			random_x_speed = random.randrange(-1,1)
			random_y_speed = random.randrange(4,10)
			meteor = Meteor(meteor_path,random_x_pos,random_y_pos,random_x_speed,random_y_speed)
			meteor_group.add(meteor)

	screen.fill((42,45,51))
	spcaceship_group.draw(screen)
	meteor_group.draw(screen)
	meteor_group.update()
	spcaceship_group.update()
	pygame.display.update() #Draw frame
	clock.tick(120) #COntrol the framerate