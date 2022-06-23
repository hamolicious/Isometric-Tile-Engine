from vector import Vec2d, Color
import pygame
from isometricTileMap.config_manager import ConfigManager
from isometricTileMap.globals import Globals
from isometricTileMap.image_loader import FrameManager
from isometricTileMap.utils import grid_to_screen, screen_to_grid
from isometricTileMap.sat import separating_axis_theorem


class Tile:
	offset: Vec2d = Vec2d(0, 0)

	def __init__(self, pos: Vec2d, frame: FrameManager) -> None:
		self.frame = frame
		self.grid_pos = Vec2d(pos)
		self.tile_size = Vec2d(ConfigManager.get_config('tile-size'))

		self.__debug_draw_rect = False
		self.__debug_draw_polygon = True

		self.__polygon = []
		self.__unit_polygon = []

		self.__generate_base_polygon()

	@property
	def screen_pos(self) -> Vec2d:
		return grid_to_screen(self.grid_pos, self.tile_size) + Tile.offset

	def __generate_base_polygon(self):
		top_left = Vec2d.zero()
		top_middle = Vec2d(top_left.add(self.tile_size.w / 2, 0))
		center_center = self.tile_size.div(2)
		half_y_diff = abs(top_middle.y - center_center.y) / 2

		# calculate from origin
		self.__unit_polygon = [
			top_middle,
			Vec2d(self.tile_size.w, half_y_diff),
			center_center,
			Vec2d(0, half_y_diff),
		]

	def offset_polygon(self):
		self.__polygon = list(map(lambda v: v.add(self.screen_pos).as_ints(), self.__unit_polygon))

	def is_hovered(self):
		mouse_polygon = Globals.get_value('mouse-pos')
		self.offset_polygon()

		return separating_axis_theorem(
			[
				mouse_polygon.add(0, 0).as_ints(),
				mouse_polygon.add(1, 0).as_ints(),
				mouse_polygon.add(0, 1).as_ints(),
			],
			self.__polygon
		)

	def update(self):
		pass

	def display(self, screen: pygame.Surface) -> None:
		self.frame.display(screen, self.screen_pos.as_ints())

		if (self.__debug_draw_rect):
			pygame.draw.rect(screen, (255, 255, 255), (
				self.screen_pos.as_ints(),
				self.tile_size.as_ints(),
			), 1)

		if (self.__debug_draw_polygon and self.is_hovered()):
			pygame.draw.polygon(screen, (255, 255, 255), self.__polygon, 1)





