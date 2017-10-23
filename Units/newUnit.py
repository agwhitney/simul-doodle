import pygame


class Unit(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([50, 50])
		self.image.fill((0, 0, 0))
		self.rect = self.image.get_rect()
		# self.selected
		self.target_x = 0
		self.target_y = 0

		self.rect.x, self.rect.y = 0, 0

	def move(self):
		if self.rect.x < self.target_x:
			self.rect.x += 1
		elif self.rect.x > self.target_x:
			self.rect.x -= 1

		if self.rect.y < self.target_y:
			self.rect.y += 1
		elif self.rect.y > self.target_y:
			self.rect.y -= 1
