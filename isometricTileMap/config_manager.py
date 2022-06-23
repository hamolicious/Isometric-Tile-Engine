from vector import Vec2d

class ConfigManager:
	config = {
		'tile-size': {
			'type': Vec2d,
			'value': Vec2d(32)
		},
		'delta-time': {
			'type': float,
			'value': 0
		},
		'frame-rate': {
			'type': int,
			'value': 60
		}
	}

	@staticmethod
	def set_config(conf, value):
		conf_body = ConfigManager.config.get(conf)

		if conf_body is None:
			raise Exception(f'Config "{conf}" is not found')

		if not (type(value) is conf_body.get('type')):
			raise Exception(f'Value "{value}" does not match type "{conf_body.get("type")}"')

		ConfigManager.config[conf]['value'] = value

	@staticmethod
	def get_config(conf):
		conf_body = ConfigManager.config.get(conf)

		if conf_body is None:
			raise Exception(f'Config "{conf}" is not found')

		return conf_body.get('value')
