import pygame
from os import walk


def get_frames(path) -> list[pygame.Surface]:
    frames = []
    for files in walk(path):
        for file in files:
            image = pygame.image.load(path +"\\" + file).convert_alpha()
            frames.append(image)
    return frames
