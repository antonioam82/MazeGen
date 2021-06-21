import pygame
import time
import random

WIDTH = 500
HEIGHT = 600
FPS = 30

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Maze Grnerator")
clock = pygame.time.Clock()
