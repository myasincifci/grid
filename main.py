import pygame
import math

from typing import Tuple, Dict

background_colour = (0, 0, 0)
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('GRID')

screen.fill(background_colour)

cubes = {}

def round_mouse(pos: Tuple[int, int]):
    x = math.floor(pos[0]/50)*50
    y = math.floor(pos[1]/50)*50

    return (x, y)


def can_draw(pos: Tuple[int, int]):
    for _, v in cubes.items():
        if pos == v:
            return False

    return True

def is_neighbour(pos: Tuple[int, int]):
    if len(cubes) == 0:
        return True
    else:
        for _, v in cubes.items():
            x, y = pos
            xv, yv = v

            if ((x == xv-50 or x == xv+50) and y == yv) != ((y == yv-50 or y == yv+50) and x == xv):
                return True

def add_cube():
    mouse_pos = round_mouse(pygame.mouse.get_pos())

    if pygame.mouse.get_pressed()[0]:
        if can_draw(mouse_pos) and is_neighbour(mouse_pos):
            x, y = round_mouse(pygame.mouse.get_pos())
            cubes[len(cubes)] = (x, y)
            
            print('##########')
            for k, v in cubes.items():    
                print(k, v)
            print('##########')

def draw_cubes():
    for _, v in cubes.items():
        rect = pygame.Rect(*v, 50, 50)
        pygame.draw.rect(screen, (255, 0, 0), rect, 3)
            
running = True
while running:
    screen.fill(background_colour)

    mouse_rect = pygame.Rect(*round_mouse(pygame.mouse.get_pos()), 50, 50)
    pygame.draw.rect(screen, (100, 100, 100), mouse_rect, 3)

    add_cube()
    draw_cubes()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
