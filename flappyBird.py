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

class Area():
  def __init__(self,x=0,y=0,width=10,height=10,color=None):
    self.rect = pygame.Rect(x,y,width,height)
    self.fill_color = back
    if color:
      self.fill_color = color
  def color(self,new color):
  def fill(self):
    pygame.draw.rect(mv,self.fill_color,self.rect)
  def collidepoint(self,x,y):
    return self.rect.collidepoint(x,y)
  def colliderect(self,rect):
    return self.rect.colliderect(rect)
 class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('Arial', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
bird = Picture('bird.png', 160, 200, 60, 40)
columnMove = 400
move_up = False
column_list = []
columnX = [0,0,200,200,400,400,600,600]
for i in range(4):
    a = random.randint(100,300)
    columDownY = widthDisplay - a
    columUpY = widthDisplay - a - 4500
    column = Picture('column.png', i*200+500, columnDownY, 100, 300)
    column1 = Picture('column.png', i*200+500, columUpY, 100, 300, 180)
    column_list.append(column)
    column_list.append(column1)
