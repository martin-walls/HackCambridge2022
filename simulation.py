import pygame
import sys

import backend

SIZE = (backend.WIDTH, backend.HEIGHT)

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

drone_img = pygame.image.load("drone.png").convert_alpha()
DRONE_IMG_WIDTH = 50
drone_img = pygame.transform.scale(drone_img, (DRONE_IMG_WIDTH, DRONE_IMG_WIDTH))


def draw_person(person):
    # pygame.draw.circle(screen, PERSON_FILL, pos, 5, 0)
    surface.blit(person_img, person.returnCoords())


def draw_drone(drone):
    # pygame.draw.circle(surface, DRONE_FILL, drone.returnCoords(), DRONE_DOT_RADIUS, 0)
    drone_coords = drone.returnCoords()
    image_coords = (drone_coords[0] - DRONE_IMG_WIDTH/2, drone_coords[1] - DRONE_IMG_WIDTH/2)
    surface.blit(drone_img, image_coords)
    pygame.draw.circle(surface, DRONE_SEARCH_RADIUS_COLOR, drone.returnCoords(), drone.getSearchRadius(), 1)


def render(person_list, drone_list):
    surface.fill(OCEAN)

    for person in person_list:
        draw_person(person)

    for drone in drone_list:
        draw_drone(drone)

    screen.blit(surface, (0,0))

    pygame.display.update()
    fps.tick(30)



if __name__ == "__main__":

    alg = "basic"
    num_drones = 3
    num_people = 1

    # allow running simulation with argument specifying which search algorithm to use
    if len(sys.argv) >= 2:
        alg = sys.argv[1].lower()
        if len(sys.argv) >= 3:
            num_drones = int(sys.argv[2])
            if len(sys.argv) >= 4:
                num_people = int(sys.argv[3])

    bck = backend.Backend(alg, num_drones, num_people)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        world_state = bck.update()
        render(world_state.peopleList, world_state.droneList)
