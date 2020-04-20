import pygame
import sys

#define bird class 
class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect(65,50,50,50)
        self.birdStatus = [pygame.image.load("flappybirdassets/assets/1.png"),
                           pygame.image.load("flappybirdassets/assets/2.png"),
                           pygame.image.load("flappybirdassets/assets/dead.png")]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False

    def birdUpdate(self):
        #movement
        if self.jump:
           self.jumpSpeed -= 1
           self.birdY -= self.jumpSpeed
        else:
           self.gravity += 0.2
           self.birdY += self.gravity
        self.birdRect[1] = self.birdY

def createMap():                  
        screen.blit(background,(0,0))
        #display pine
        screen.blit(Pipeline.pineUp,(Pipeline.wallx, -300))
        screen.blit(Pipeline.pineUp,(Pipeline.wallx, 500))
        Pipeline.PipelineUpdate()
        #display bird
        if Bird.dead :
            Bird.status = 2
        elif Bird.jump :
            Bird.status = 1
        screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX,Bird.birdY))
        Bird.birdUpdate()

        screen.blit(font.render('Score:'+ str(score),1,(255,255,255)),(100,50))
        pygame.display.update()

#define pipeline class
class Pipeline(object):
    def __init__(self):
        self.wallx = 400
        self.pineUp = pygame.image.load("flappybirdassets/assets/top.png")
        self.pineDown = pygame.image.load("flappybirdassets/assets/bottom.png")

    def PipelineUpdate(self):
        #movement
        self.wallx -= 5
        if self.wallx < -80:
            global score
            score += 1
            self.wallx = 400

def checkDead():
    upRect = pygame.Rect(Pipeline.wallx,-300,Pipeline.pineUp.get_width(),Pipeline.pineUp.get_height())
    downRect = pygame.Rect(Pipeline.wallx,500,Pipeline.pineDown.get_width(),Pipeline.pineDown.get_height())

    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
    if not Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False

def getResult():
    final_text1 = "GAME OVER"
    final_text2 = "Your final score is :" + str(score)
    ft1_font = fit1_font = pygame.font.SysFont("Arial",70)
    ft1_surf = font.render(final_text1,1,(242,3,36))
    ft2_font = fit2_font = pygame.font.SysFont("Arial",50)
    ft2_surf = font.render(final_text2,1,(253,177,6))

    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,200])
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    font = pygame.font.SysFont(None,50)

    size = width, height = 400,650
    screen = pygame.display.set_mode(size) #setting windows sieze
    clock = pygame.time.Clock()# setting delay time
    color = (255,255,255)

    Bird = Bird()
    Pipeline = Pipeline()
    score = 0

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN) and not Bird.dead :
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpSpeed = 10


        # screen.fill(color)
        background = pygame.image.load("flappybirdassets/assets/background.png")
        if checkDead():
            getResult()
        else:
            createMap()

pygame.quit()

