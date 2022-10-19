#!/usr/bin/env python3
import pygame
# set up a screen 
screen = [1, 1, 2, 2, 2, 1]
#print(screen)

# player on screen
screen[3] = 8
#print(screen)

# keep record of player poisition
playerpos = 3 
screen[playerpos] = 8 
#print(screen)

# move player to new position w/o erasing old
playerpos = playerpos - 1
screen[playerpos] = 8 
#print(screen)

# creating map to allow movement with no trace of old 
background = [1, 1, 2, 2, 2, 1]
screen = [0] * 6  
for i in range(6): 
	screen[i] = background[i]
#print(screen)
playerpos = 3 
screen[playerpos] = 8 
#print(screen)

# making player move take 2 
#print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1 
screen[playerpos] = 8 
#print(screen)

# move player to the left 
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
#print(screen)

#using graphics
# load graphics into terrain1, terrain2, and player image 
# background = [terrain1, terrain1, terrain2, terrain2, terrain2, terain1]
# screen = create_graphics_screen()
# for i in range(6):
# 	screen.blit(background[i], (i*10, 0))
# playerpos = 3
# screen.blit(playerimage, (playerpos*10, 0))
# playerpos = playerpos - 1
# screen.blit(playerimage, (player * 10, 0))

# smooth movement
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()				# get a pygame clock object
player = load_player_image(hero_image.jpeg)
background = load_background_image(background-image-galaxy.gif)
screen.blit(background, (0, 0))				# draw the background
position = player.get_rect()
screen.blit(player, position)			# draw the player 
pygame.display.update()		# and show it all
for x in range(100):			# animate 100 frames
	screen.blit(background, position, position)			#erase
	position = position.move(2, 0)			# move player
	screen.blit(player, position)			# draw new player
	pygame.display.update()			# and show it all
	clock.tick(60)			#update 60 times per second
