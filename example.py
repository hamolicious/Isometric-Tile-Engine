import os
import pygame
from time import time
from vector import Vec2d
from isometricTileMap import Tile
from isometricTileMap.config_manager import ConfigManager
from isometricTileMap.globals import Globals
from isometricTileMap.image_loader import ImageLoader
from isometricTileMap.utils import screen_to_grid
from isometricTileMap.world import World

#region pygame init
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 0

delta_time = 0 ; frame_start_time = 0
#endregion

ImageLoader.load_images_from_directory(path='Tiles/Basic')
world = World()
ConfigManager.set_config('tile-size', Vec2d(32))
CHUNK_SIZE = 10

for i in range(0, CHUNK_SIZE):
	for j in range(0, CHUNK_SIZE):
		world.add_tile(Tile(Vec2d(i, j), ImageLoader.select_random_image_from([
			'grass',
			'dirt',
			'blue_flowers',
			'red_flowers',
			'yellow_flowers',
			'house',
		])))

world.offset = Vec2d(size).div(2)

counter = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	frame_start_time = time()
	screen.fill(0)

	mouse_pos   = Vec2d(pygame.mouse.get_pos())
	mouse_press = pygame.mouse.get_pressed()
	key_press   = pygame.key.get_pressed()

	Globals.set_value('mouse-pos', mouse_pos)

	if key_press[pygame.K_ESCAPE] : pygame.quit() ; quit()

	if key_press[pygame.K_LEFT] : world.offset.x -= 100 * delta_time
	if key_press[pygame.K_RIGHT] : world.offset.x += 100 * delta_time
	if key_press[pygame.K_UP] : world.offset.y -= 100 * delta_time
	if key_press[pygame.K_DOWN] : world.offset.y += 100 * delta_time
	world.update_offset()

	world.display(screen)

	pygame.display.update()
	clock.tick(fps)
	delta_time = time() - frame_start_time
	Globals.set_value('delta-time', delta_time)
	Globals.set_value('frame-rate', int(clock.get_fps()))
	pygame.display.set_caption(f'Framerate: {int(clock.get_fps())}')
