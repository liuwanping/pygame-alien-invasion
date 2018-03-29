class Settings():
	def __init__(self):
		#screen settings
		self.screen_width = 600
		self.screen_height = 500
		self.bg_color = (230,230,230)
		self.ship_limit = 3
		
		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 6

		#alien settings
		self.fleet_drop_speed = 10


		self.speed_scale = 1.1
	
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 0.5
		self.alien_speed_factor = 0.5
		self.fleet_direction = 1 # 1:right, -1:left
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speed_scale
		self.bullet_speed_factor *= self.speed_scale
		self.alien_speed_factor *= self.speed_scale



