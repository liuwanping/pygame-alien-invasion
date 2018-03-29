import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
	#init the game, create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#create "Play"button
	play_button = Button(ai_settings,screen,"Play")

	#create a ship
	ship=Ship(ai_settings,screen)

	#create bullets
	bullets=Group()

	#create aliens
	aliens = Group() 
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	stats = GameStats(ai_settings)	
	
	sb = Scoreboard(ai_settings,screen,stats)

	#start the main game loop
	while True:
		gf.check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button)
		
		if stats.game_active:

			ship.update()

			gf.update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb)

			gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets)

		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,sb)

run_game()

	
