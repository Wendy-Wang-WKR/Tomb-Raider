import pygame

camera = pygame.Rect(0, 0, 0, 0)

def create_screen(width, height, title):
    pygame.display.set_caption(title)

    screen = pygame.display.set_mode((width, height))
    camera.height = height
    camera.width = width
    return screen