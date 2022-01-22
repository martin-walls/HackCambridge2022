import pygame
import sys

import backend

SIZE = width, height = 700,500

# COLORS
OCEAN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255, 255, 255)

PERSON_FILL = BLACK
DRONE_FILL = WHITE
DRONE_SEARCH_RADIUS = (255,255,255,128)

screen = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()


def draw_person(pos):
    pygame.draw.circle(screen, PERSON_FILL, pos, 5, 0)

def draw_drone(pos, search_radius):
    pygame.draw.circle(screen, DRONE_FILL, pos, 3, 0)
    pygame.draw.circle(screen, DRONE_SEARCH_RADIUS, pos, search_radius, 1)

def render(person_pos, drone_pos):
    screen.fill(OCEAN)
    draw_person(person_pos)
    for drone in drone_pos:
        draw_drone(drone, 10)
    pygame.display.update()
    fps.tick(60)




if __name__ == "__main__":

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        attrs = backend.update()
        render(attrs.person_pos, attrs.drone_positions)
