import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
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

	#creat aliens
	aliens = Group() 
	gf.creat_fleet(ai_settings,screen,ship,aliens)
	
	stats = GameStats(ai_settings)	

	#start the main game loop
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)

		ship.update()

		gf.update_bullets(aliens,bullets)

		gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets)

		gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()

	
