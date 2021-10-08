import pygame
from math import ceil
from os import walk

def get_frames(path) -> list[pygame.Surface]:
    frames = []
    for _, __, files in walk(path):
        for file in files:
            image = pygame.image.load(path +"\\" + file).convert_alpha()
            image = pygame.transform.scale2x(image)
            frames.append(image)
    return frames

def fill_whith_image(surface: pygame.Surface, image: pygame.Surface) -> None:
    surface_x, surface_y = surface.get_size()
    image_x, image_y = image.get_size()
    num_x = ceil(surface_x / image_x)
    num_y = ceil(surface_y / image_y)
    for i in range(num_y):
        for j in range(num_x):
            pos = (j * image_x, i * image_y)
            surface.blit(image,pos)