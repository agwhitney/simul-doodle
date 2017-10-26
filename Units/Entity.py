import pygame


class Entity(pygame.sprite.Sprite):
	def __init__(self, x, y, selected=False):
		super().__init__()
		self.image = pygame.image.load("assets/meep.png")
		self.rect = self.image.get_rect()
		self.rect.x = x  # Initial position of sprite
		self.rect.y = y
		self.selected = selected  # Boolean for if unit is selected

	def move(self, target_x, target_y):
		"""Move the unit towards a target coordinate.
		dx/dy is in pixels, and travels that many pixels per tick,
		but it probably shouldn't be hard-coded here.
		"""
		if not target_x or not target_y:
			# Based on a last-click, which starts the game as position (None, None)
			# It's janky and I don't like it.
			return

		if self.rect.x < target_x:
			self.rect.x += 1
		elif self.rect.x > target_x:
			self.rect.x -= 1

		if self.rect.y < target_y:
			self.rect.y += 1
		elif self.rect.y > target_y:
			self.rect.y -= 1
