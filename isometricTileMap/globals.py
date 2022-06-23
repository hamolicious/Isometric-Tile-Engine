from vector import Vec2d

class Globals:
	values = {
		'frame-rate': {
			'type': int,
			'value': 0
		},
		'delta-time': {
			'type': float,
			'value': 0
		},
		'mouse-pos': {
			'type': Vec2d,
			'value': Vec2d.zero()
		},
	}

	@staticmethod
	def set_value(conf, value):
		conf_body = Globals.values.get(conf)

		if conf_body is None:
			raise Exception(f'Config "{conf}" is not found')

		if not (type(value) is conf_body.get('type')):
			raise Exception(f'Value "{value}" does not match type "{conf_body.get("type")}"')

		Globals.values[conf]['value'] = value

	@staticmethod
	def get_value(conf):
		conf_body = Globals.values.get(conf)

		if conf_body is None:
			raise Exception(f'Config "{conf}" is not found')

		return conf_body.get('value')
