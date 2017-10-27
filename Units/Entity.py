import pygame
import random

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Entity(pygame.sprite.Sprite):
	def __init__(self, x, y, image, selected=False, ai_component=None):
		super().__init__()

		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.selected = selected  # Boolean for if unit is selected

		self.ai_component = ai_component
		if self.ai_component:
			self.ai_component.owner = self

	def move(self, dx, dy):
		self.rect.x += dx
		self.rect.y += dy

	def move_towards(self, target_x, target_y):
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

		dx, dy = 0, 0

		if center_x < target_x:
			dx += 1
		elif center_x > target_x:
			dx -= 1

		if center_y < target_y:
			dy += 1
		elif center_y > target_y:
			dy -= 1

		self.move(dx, dy)

	def update(self, target_xy=None):
		"""pygame.sprite.Sprite update function can be called by/as a group!"""
		if target_xy:
			self.move_towards(target_xy[0], target_xy[1])

		if self.ai_component:
			self.ai_component.update()


class PathMover:
	"""Basic mindless moving ai_component"""
	def __init__(self):
		self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

	def move_in_direction(self):
		x = self.owner.rect.x
		y = self.owner.rect.y

		if not 0 < x < SCREEN_WIDTH - self.owner.rect.width:
			self.direction[0] *= -1
		if not 0 < y < SCREEN_HEIGHT - self.owner.rect.height:
			self.direction[1] *= -1

		dx = self.direction[0]
		dy = self.direction[1]

		self.owner.move(dx, dy)

	def update(self):
		self.move_in_direction()
