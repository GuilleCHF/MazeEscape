import pygame
from os import walk

def get_frames(path) -> list[pygame.Surface]:
    frames = []
    for _, __, files in walk(path):
        for file in files:
            image = pygame.image.load(path +"\\" + file).convert_alpha()
            image = pygame.transform.scale2x(image)
            frames.append(image)
    return frames
