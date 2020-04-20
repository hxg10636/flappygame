# import needed libraries.
import pygame
import sys

# initialization pygame
pygame.init()

screen = pygame.display.set_mode((320,240)) # setting the size of window

while True:
    # setting conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()
