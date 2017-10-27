import pygame
from pygame.locals import *
import random

from config import *

from Managers import GameManager
from Managers.event_handlers import handle_keys
from Map.game_map import GameMap
from Units.Entity import Entity, PathMover


if __name__ == '__main__':
	# SETTINGS
	pygame.init()
	pygame.display.set_caption("Ayy Lmao")
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], RESIZABLE)
	clock = pygame.time.Clock()
	done = False
	ticks = 0

	# MAP AND UNIT INITIALIZE
	game_map = GameMap(MAP_WIDTH, MAP_HEIGHT, TILE_WIDTH, TILE_HEIGHT)

	player = Entity(0, 0, "assets/meep.png")
	player_group = pygame.sprite.GroupSingle()
	player_group.add(player)

	apple_group = pygame.sprite.Group()
	for n in range(5):
		x = random.randint(0, SCREEN_WIDTH-80)
		y = random.randint(0, SCREEN_HEIGHT-80)
		apple = Entity(x, y, "assets/meep.png", ai_component=PathMover())
		apple_group.add(apple)

	# STORAGE
	last_left_click = [None, None]  # Last position clicked with LMB

	while not done:
		for event in pygame.event.get():
			quit_game = handle_keys(event).get('quit')
			resize = handle_keys(event).get('resize')
			lmb_down = handle_keys(event).get('lmb_down')

			if quit_game:
				done = True
			if resize:
				screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
			if lmb_down:
				last_left_click = event.pos

		# MANAGE AND UPDATE - WILL BE SEPARATED TBD
		player_group.update(last_left_click)
		apple_group.update()
		game_map.draw(screen)
		player_group.draw(screen)
		apple_group.draw(screen)
		pygame.display.update()  # No args: same as flip

		clock.tick(60)  # TODO make this scale w user selected speed somehow
