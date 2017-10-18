import pygame


class Tile:
	def __init__(self, x, y, width, height, terrain, movement_mod, color):
		self.rect = pygame.Rect(x, y, width, height)
		self.terrain = terrain
		self.movement_mod = movement_mod
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
