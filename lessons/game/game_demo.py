import pygame
import sys
from random import randint

# starts window
pygame.init()
#  constants to define window size and set FPS
HEIGHT = 450
WIDTH = 800
FPS = 60
BACKGROUND_COLOR = (53, 130, 27)
APPLE_COLOR = (200, 50, 50)
apple: pygame.Rect = pygame.Rect(200, 400, 20, 20)

basket: pygame.Rect = pygame.Rect(WIDTH -110, HEIGHT - 80, 100, 50 )
#create clock object to limiT FPS
FramePerSec = pygame.time.Clock()

#create surafce to draw objects open
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

while True:

    for event in pygame.event.get():
        #this allows you to close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(apple.collidepoint(pos)): # this method checks whther a point is inside the rectangle
                holding_apple = not holding_apple

    if holding_apple:
        pos = pygame.mouse.get_pos()
        if (pos.y > HEIGHT-100):
            apple.center = pos

    displaysurface.fill((BACKGROUND_COLOR))
    pygame.draw.circle(displaysurface, APPLE_COLOR, apple.center, apple.width/2)
    pygame.draw.rect(displaysurface, BASKET_COLOR, basket)

    pygame.display.update()
    FramePerSec.tick(FPS)