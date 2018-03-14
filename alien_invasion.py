import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	#init the game, creat a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#creat a ship
	ship=Ship(ai_settings,screen)

	#creat bullets
	bullets=Group()

	#start the main game loop
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)

		ship.update()
		gf.update_bullets(bullets)

		gf.update_screen(ai_settings,screen,ship,bullets)

run_game()

	
