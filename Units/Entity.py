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
			# This is a catch but I think it's janky and don't like it.
			return

		center_x = self.rect.center[0]
		center_y = self.rect.center[1]

		if center_x < target_x:
			self.rect.x += 1
		elif center_x > target_x:
			self.rect.x -= 1

		if center_y < target_y:
			self.rect.y += 1
		elif center_y > target_y:
			self.rect.y -= 1
