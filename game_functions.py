import sys

import pygame

from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True	
	elif event.key == pygame.K_UP:
		ship.moving_up = True	
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True	
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left =False
	elif event.key == pygame.K_UP:
		ship.moving_up = False	
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets):
	#monitor kayboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship,bullets,aliens):
	#redraw the screen every loop		
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	
	aliens.draw(screen)

	#make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def get_numbers_alien_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width-2*alien_width
	numbers_alien_x = int(available_space_x / (2*alien_width))
	return numbers_alien_x

def get_numbers_row(ai_settings,ship_height,alien_height):
	available_sapce_y = ai_settings.screen_height-(3*alien_height)-ship_height
	numbers_row = int(available_sapce_y / (2*alien_height))
	return numbers_row

def creat_alien(ai_settings,screen,alien_number,row_number,aliens):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width+2*alien_width*alien_number 
	alien.rect.y= alien.rect.height+2*alien.rect.height* row_number
	alien.rect.x=alien.x
	aliens.add(alien)

def creat_fleet(ai_settings,screen,ship,aliens):
	print("creat_fleet")
	alien = Alien(ai_settings,screen)
	numbers_alien_x = get_numbers_alien_x(ai_settings,alien.rect.width)
	numbers_row = get_numbers_row(ai_settings,ship.rect.height,alien.rect.height)
	print("numbers_alien_x")
	print(numbers_alien_x)
	print("numbers_row")
	print(numbers_row)
	for row_number in range(numbers_row):
		for alien_number in range(numbers_alien_x):
			creat_alien(ai_settings,screen,alien_number,row_number,aliens)

