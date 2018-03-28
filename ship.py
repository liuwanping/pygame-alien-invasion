import pygame

class Ship():
 	def __init__(self,ai_settings,screen):
		#init ship and set its location
		self.screen = screen
		self.ai_settings=ai_settings

		#load ship image and draw rect
		self.image=pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#put new ship on the bottom and center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom

		#store decimal
		self.center_x=float(self.rect.centerx)
		self.center_y=float(self.rect.centery)

		#moving sign
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def center_ship(self):
		self.center_x = self.screen_rect.centerx
		self.center_y = self.ai_settings.screen_height-0.5*self.rect.height


	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center_x +=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.center_x -=self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top>0:
			self.center_y -=self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom<self.ai_settings.screen_height:
			self.center_y +=self.ai_settings.ship_speed_factor
	
		self.rect.centerx=self.center_x
		self.rect.centery=self.center_y

	def blitme(self):
		self.screen.blit(self.image,self.rect)


