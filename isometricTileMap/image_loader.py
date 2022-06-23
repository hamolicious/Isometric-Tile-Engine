import random
import pygame
import os
from isometricTileMap.frame_manager import FrameManager

class ImageLoader:
	images = {}

	@staticmethod
	def get_random_image() -> pygame.Surface:
		return random.choice([ImageLoader.images[key] for key in ImageLoader.images])

	@staticmethod
	def select_random_image_from(collection: list[pygame.Surface]) -> pygame.Surface:
		return random.choice([ImageLoader.images[key] for key in collection])

	@staticmethod
	def get_image(name: str) -> pygame.Surface:
		if name in ImageLoader.images:
			return ImageLoader.images[name]
		else:
			raise Exception(f'Image "{name}" not found.')

	@staticmethod
	def load_images_from_directory(path: str = 'Tiles') -> None:
		for file in os.listdir(path):
			full_path = os.path.join(path, file)

			if (os.path.isdir(full_path)):
				frame = ImageLoader.__load_image_sequence(full_path)
			else:
				frame = ImageLoader.__load_image(full_path)

			name = ImageLoader.__generate_name_from_file(file)
			ImageLoader.images[name] = frame

	@staticmethod
	def __generate_name_from_file(file: str) -> str:
		return file.split('.')[0].lower()

	@staticmethod
	def __load_image_sequence(path: str) -> pygame.Surface:
		frames = []
		for file in os.listdir(path):
			frames.append(
				pygame.image.load(os.path.join(path, file))
			)
		return FrameManager(frames)

	@staticmethod
	def __load_image(path: str) -> pygame.Surface:
		source_image = pygame.image.load(path)
		return FrameManager([source_image])

