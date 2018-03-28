import sys

import pygame

from time import sleep

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


def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button):
	#redraw the screen every loop		
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	
	aliens.draw(screen)
	
	if not stats.game_active:
		play_button.draw_button()
	#make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # Destroy existing bullets, and create new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

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
	alien = Alien(ai_settings,screen)
	numbers_alien_x = get_numbers_alien_x(ai_settings,alien.rect.width)
	numbers_row = get_numbers_row(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(numbers_row):
		for alien_number in range(numbers_alien_x):
			creat_alien(ai_settings,screen,alien_number,row_number,aliens)

def check_fleet_edgs(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,aliens,ship,bullets):
	if stats.ships_left>0:
		stats.ships_left -=1

		aliens.empty()
		bullets.empty()
	
		creat_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		sleep(1)
	else:
		stats.game_active = False


def update_aliens(ai_settings,stats,screen,aliens,ship,bullets):
	check_fleet_edgs(ai_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,aliens,ship,bullets)



