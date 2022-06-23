import pygame
from isometricTileMap.config_manager import ConfigManager
import random
from vector import Vec2d

from isometricTileMap.globals import Globals

class FrameManager:
	def __init__(self, frames: list[pygame.Surface]) -> None:
		self.frames = frames
		self.max_frames = len(self.frames)

		self.frame_offset = random.randint(0, self.max_frames)
		self.current_frame = 0#self.frame_offset
		self.__clamp_current_frame()

		self.offset = self.__calculate_offset()

	def __calculate_offset(self):
		return Vec2d(self.frames[0].get_size()) \
			.div(ConfigManager.get_config('tile-size')) \
			.sub(1) \
			.mult(-1) \
			.mult(ConfigManager.get_config('tile-size'))

	def __clamp_current_frame(self) -> None:
		if self.current_frame >= self.max_frames:
			self.current_frame = 0

	def __calculate_delta_frame(self):
		return 0.15 * Globals.get_value('delta-time')

	def next_frame(self):
		delta_frame = self.__calculate_delta_frame()
		self.current_frame += delta_frame
		self.__clamp_current_frame()

	def display(self, screen: pygame.Surface, pos: Vec2d) -> None:
		screen.blit(self.frames[int(self.current_frame)], Vec2d(pos).add(self.offset).as_ints())
		self.next_frame()

