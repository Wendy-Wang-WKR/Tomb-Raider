import pygame
from src.core.camera import camera

sprites = []
loaded = {}

image_folder_location  = "content/img"
class Sprite:
    def __init__(self, image):
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_folder_location + "/" + image)
            loaded[image] = self.image
        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))