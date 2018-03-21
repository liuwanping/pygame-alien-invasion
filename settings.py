class Settings():
	def __init__(self):
		#screen settings
		self.screen_width = 600
		self.screen_height = 500
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		#bullet settings
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 6

		#alien settings
		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 # 1:right, -1:left



