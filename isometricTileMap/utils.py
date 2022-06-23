from vector import Vec2d

def grid_to_screen(pos: Vec2d, tile_size: Vec2d) -> Vec2d:
	pos = Vec2d(pos)
	tile_size = Vec2d(tile_size)
	return Vec2d(
		(pos.x - pos.y) * tile_size.w / 2,
		(pos.x + pos.y) * tile_size.h / 4,
	)

def screen_to_grid(pos: Vec2d, tile_size: Vec2d) -> Vec2d:
	pos = Vec2d(pos)
	tile_size = Vec2d(tile_size)

	return Vec2d(
		(pos.x / (tile_size.w / 4) + pos.y / (tile_size.h / 2)) / 2,
		(pos.y / (tile_size.h / 2) - (pos.x / (tile_size.w / 4))) / 2
	).add(0.5)
