import pygame
import sys

import backend

SIZE = width, height = 700, 500

# COLORS
OCEAN = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PERSON_FILL = BLACK
DRONE_FILL = WHITE
DRONE_SEARCH_RADIUS = (255, 255, 255, 128)

screen = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()

person_img = pygame.image.load("sadface.png").convert_alpha()
person_img = pygame.transform.scale(person_img, (68,62))


def draw_person(person):
    # pygame.draw.circle(screen, PERSON_FILL, pos, 5, 0)
    screen.blit(person_img, person.returnCoords())


def draw_drone(drone):
    pygame.draw.circle(screen, DRONE_FILL, drone.returnCoords(), 3, 0)
    pygame.draw.circle(screen, DRONE_SEARCH_RADIUS, drone.returnCoords(), 10, 1)


def render(person_list, drone_list):
    screen.fill(OCEAN)

    for person in person_list:
        draw_person(person)

    for drone in drone_list:
        draw_drone(drone)

    pygame.display.update()
    fps.tick(60)


# def render(person_pos, drone_pos):
#     screen.fill(OCEAN)
#     draw_person(person_pos)
#     for drone in drone_pos:
#         draw_drone(drone, 10)
#     pygame.display.update()
#     fps.tick(60)


if __name__ == "__main__":

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        attrs = backend.update()
        render(attrs.peopleList, attrs.droneList)
