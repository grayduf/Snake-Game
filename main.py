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

