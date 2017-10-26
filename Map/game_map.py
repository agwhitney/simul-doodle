from Map.tile_types import tile_list
import random


class GameMap:
	def __init__(self, width, height, tile_width, tile_height):
		self.width = width
		self.height = height
		self.tile_width = tile_width
		self.tile_height = tile_height

		self.tile_list = tile_list()
		self.map = self.create_new_map()

	def random_tile(self, x, y):
		"""Returns a tile object chosen at random from the tile_list"""
		tile_number = random.randint(0, len(self.tile_list) - 1)
		return self.tile_list[tile_number](x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height)

	def create_new_map(self):
		"""Returns a new map; a 2d list of tile objects"""
		new_map = []

		for x in range(self.width):
			new_map.append([])
			row = new_map[x]
			for y in range(self.height):
				row.append([])
				row[y] = self.random_tile(x, y)

		return new_map

	def draw(self, screen):
		screen.fill((0, 0, 0))

		for x in range(self.width):
			for y in range(self.height):
				self.map[x][y].draw(screen)
