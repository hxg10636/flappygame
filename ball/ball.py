# import needed libraries.
import pygame
import sys

# initialization pygame
pygame.init()

size = width, height = 640,480
screen = pygame.display.set_mode((size)) # setting the size of window
ball = pygame.image.load('flappybirdassets/assets/ball.png') # loading assets
ballre = pygame.transform.scale(ball, (111,111)) # resize the ball
ballrect = ballre.get_rect()
speed = [5,5] # setting X and Y.

clock = pygame.time.Clock()
color = (0,0,0)
while True:
    clock.tick(60) # run 60 times every second
    # setting conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    # checking detction
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top <0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)
    screen.blit(ballre,ballrect)
    pygame.display.flip()

pygame.quit()
