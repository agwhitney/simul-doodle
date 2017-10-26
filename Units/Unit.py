import pygame


class Unit:
	"""Units should probably be represented as pygame.Sprite objects.
	I'm not quite sure how best to do that, yet, but it'll get there.
	"""
	def __init__(self, x, y, radius):
		self.x = self.targetX = x
		self.y = self.targetY = y
		self.radius = radius
		self.selected = False

	def go_to(self, game_map, targetX, targetY):
		"""Gather a new coordinate to move towards"""
		# if not self.selected:
		# 	return

		if -1 < targetX < game_map.width:
			self.targetX = targetX
		if -1 < targetY < game_map.height:
			self.targetY = targetY

	def move(self):
		"""Moving function, called each logic cycle"""
		if self.x < self.targetX:
			self.x += 1
		elif self.x > self.targetX:
			self.x -= 1

		if self.y < self.targetY:
			self.y += 1
		elif self.y > self.targetY:
			self.y -= 1

	def get_screen_loc(self, game_map):
		return (self.x * game_map.tile_width + int(game_map.tile_width / 2),
				self.y * game_map.tile_height + int(game_map.tile_height / 2))

	def draw(self, screen, game_map):
		# TODO ADAM could screen position be gathered without utilizing map details?
		pygame.draw.circle(screen, (0, 0, 0), self.get_screen_loc(game_map), self.radius)

	def update(self, screen, game_map):
		self.move()
		# TODO check to make sure we are inbounds here
		self.draw(screen, game_map)
