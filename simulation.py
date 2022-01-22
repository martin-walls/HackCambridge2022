import pygame
import sys

import backend

SIZE = width, height = 1400, 1000

# COLORS
OCEAN = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PERSON_FILL = BLACK
DRONE_FILL = WHITE
DRONE_SEARCH_RADIUS_COLOR = (156,156,255)
DRONE_DOT_RADIUS = 5

screen = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()

surface = pygame.Surface(SIZE, pygame.SRCALPHA)

person_img = pygame.image.load("sadface.png").convert_alpha()
person_img = pygame.transform.scale(person_img, (68,62))


def draw_person(person):
    # pygame.draw.circle(screen, PERSON_FILL, pos, 5, 0)
    surface.blit(person_img, person.returnCoords())


def draw_drone(drone):
    pygame.draw.circle(surface, DRONE_FILL, drone.returnCoords(), DRONE_DOT_RADIUS, 0)
    pygame.draw.circle(surface, DRONE_SEARCH_RADIUS_COLOR, drone.returnCoords(), drone.getSearchRadius(), 1)


def render(person_list, drone_list):
    surface.fill(OCEAN)

    for person in person_list:
        draw_person(person)

    for drone in drone_list:
        draw_drone(drone)

    screen.blit(surface, (0,0))

    pygame.display.update()
    fps.tick(60)



if __name__ == "__main__":

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        attrs = backend.update()
        render(attrs.peopleList, attrs.droneList)
