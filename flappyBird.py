import pygame
import random
pygame.init()

widthDisplay = 500
heightDisplay = 500

back = (200, 255, 255)
mw = pygame.display.set_mode((widthDisplay, heightDisplay))
mw.fill(back)
clock = pygame.time.Clock()


game = True



























#8
if move_up:
  bird.rect.y -=10
for i in column_list:
  if i.rect.colliderect(bird.rect):
    game = False
if bird.rect.y > 500 or bird.rect.y < 0:
  game = False
pygame.display.update()
clock.tick(40)
