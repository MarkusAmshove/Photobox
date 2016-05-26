import random


RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [RED, WHITE, GREEN, BLUE]


def randomcolor_predefined():
    return colors[random.randint(0, len(colors) - 1)]


def randomcolor_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))