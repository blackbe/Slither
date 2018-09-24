import pygame
import time
import random
import os
import sys


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon = pygame.image.load(resource_path("icon.png"))  # should be 32 by 32
pygame.display.set_icon(icon)


img = pygame.image.load(resource_path("snakehead.png"))
appleimg = pygame.image.load(resource_path("apple.png"))


clock = pygame.time.Clock()

appleThickness = 30
block_size = 20
FPS = 10


direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)




def pause():
    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")
    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    quitScreen()
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)

        clock.tick(5)



def quitScreen():
    gameDisplay.fill(white)
    message_to_screen("Have a wonderful day!",
                      green,
                      size="medium")
    pygame.display.update()
    time.sleep(2)  # not going to keep this here
    return


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def randAppleGen():
    randAppleX = random.randrange(0, display_width - appleThickness)
    randAppleY = random.randrange(0, display_height - appleThickness)

    # to make the apple location line up correctly
    roundX = round(randAppleX)
    roundY = round(randAppleY)

    return roundX, roundY


def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitScreen()
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    quitScreen()
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          size="large")
        message_to_screen("The objective of the game is to eat red apples",
                          black,
                          -30)
        message_to_screen("The more apples you eat the longer you get.",
                          black,
                          10)
        message_to_screen("If you run into yourself or the edges, you die",
                          black,
                          50)
        message_to_screen("Press C to play, P to pause, or Q to quit",
                          black,
                          180)


        pygame.display.update()
        clock.tick(10)

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)


    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction

    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    roundX, roundY = randAppleGen()

    while not gameExit:

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              y_displace=50,
                              size="medium")
            pygame.display.update()

        while gameOver == True:
            #gameDisplay.fill(white)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(appleimg, (roundX, roundY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        score(snakeLength - 1)
        pygame.display.update()

        if lead_x > roundX and lead_x < roundX + appleThickness or lead_x + block_size > roundX and lead_x + block_size < roundX + appleThickness:
            if lead_y > roundY and lead_y < roundY + appleThickness:
                roundX, roundY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > roundY and lead_y + block_size < roundY + appleThickness:
                roundX, roundY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)

    quitScreen()
    pygame.quit()
    quit()


game_intro()
gameLoop()

