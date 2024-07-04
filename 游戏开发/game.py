import pygame
import sys
import src.core.input as input
from src.components.sprite import *
from src.core.config import *
from src.components.player import *
from src.core.map import *
from src.core.camera import create_screen
from src.components.entity import Entity, active_objects
from src.components.physics import Body
from src.core.area import Area, area
from src.data.tile_types import tile_kinds

# Setup
pygame.init()

screen = create_screen(WIN_WIDTH, WIN_HEIGHT, "Tomb Raider")

running = True

area = Area("start.map", tile_kinds)

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    # Update Code
    for a in active_objects:
        a.update()

    # Draw Code
    screen.fill(WHITE)
    area.map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()


pygame.quit()