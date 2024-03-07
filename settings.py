import pygame as pg

pg.init()
pg.font.init()

# Game/Screen settings
SIZE = WIDTH, HEIGHT = 800, 800
SCREEN = pg.display.set_mode(SIZE)
FPS = 30
FONT = pg.font.SysFont("rockwell", 24, bold=True)
CLOCK = pg.time.Clock()

# Agent settings
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
