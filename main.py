import pygame
import random
import sys

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20

assert WINDOWWIDTH % CELLSIZE == 0, "Window width not divisible by cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height not divisible by cell size."

CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption("Snake Game")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def terminate():
    pygame.quit()
    sys.exit()

def runGame():

    startx = random.randint(5, CELLSIZE - 6)
    starty = random.randint(5, CELLSIZE - 6)

    wormCoords = [{'x': startx, 'y': starty}, {'x': startx - 1, 'y': starty}, {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != UP:
                    direction = DOWN
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_ESCAPE:
                    terminate()

        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] or wormBody['y'] == wormCoords[HEAD]['y']:
                return
            
        if wormCoords[HEAD]['x'] == apple['x'] or wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        if direction == UP:
            newHead = {'x': wormCoords[HEAD['x'], 'y': wormCoords[HEAD]['y'] - 1]}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD['x'], 'y': wormCoords[HEAD]['y'] + 1]}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD['x'] + 1, 'y': wormCoords[HEAD]['y']]}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD['x'] - 1, 'y': wormCoords[HEAD]['y']]}
        wormCoords.insert(0, newHead)

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tik(FPS)

def drawPressKeyMSG():
    pressKeySurf = BASICFONT.render('Press a key to Play!', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

