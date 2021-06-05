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


class label(Area):
  def set_text((self, text, fsize=12,text_color=(0,0,0)):
               self.image= pygame.font.SysFont('Areal',fsize).render(text,True,text_color)
  def draw(self,shift_x=0,shift_y=0):
               self.fill()
               mw.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
               
