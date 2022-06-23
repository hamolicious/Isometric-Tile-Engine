import pygame
from vector import Vec2d
from isometricTileMap.tile import Tile


class World:
	def __init__(self) -> None:
		self.tiles: list[Tile] = []
		self.offset: Vec2d = Vec2d(0, 0)

	def update_offset(self):
		Tile.offset = self.offset.copy()

	def add_tile(self, new_tile: Tile):
		self.tiles.append(new_tile)

	def update_order(self):
		self.tiles.sort(key=
			lambda tile: 1/tile.screen_pos.y * tile.screen_pos.x,
			reverse=True
		)

	def display(self, screen: pygame.Surface) -> None:
		for tile in self.tiles:
			tile.display(screen)





