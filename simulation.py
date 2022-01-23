import pygame
import sys
import argparse

import backend

SIZE = (backend.WIDTH, backend.HEIGHT)

ALG_TO_USE = "basic"
NUM_DRONES = 3
NUM_PEOPLE = 1

# parse arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alg", help="Algorithm to use", type=str)
    parser.add_argument("--drones", help="Number of drones", type=int)
    parser.add_argument("--people", help="Number of people", type=int)
    parser.add_argument("--width", help="Screen width", type=int)
    parser.add_argument("--height", help="Screen height", type=int)

    args = parser.parse_args()

    print(args)

    if args.width is not None and args.height is not None:
        SIZE = (args.width, args.height)

    if args.alg is not None:
        ALG_TO_USE = args.alg.lower()

    if args.drones is not None:
        NUM_DRONES = args.drones

    if args.people is not None:
        NUM_PEOPLE = args.people


# COLORS
OCEAN = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PERSON_FILL = BLACK
DRONE_FILL = WHITE
DRONE_SEARCH_RADIUS_COLOR = (156,156,255)
DRONE_DOT_RADIUS = 5
DRONE_PATH_COLOR = (128,128,255)
DRONE_VISIBILITY_PATH_COLOR = (50,50,255)

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
    drone_coords = drone.returnCoords()
    image_coords = (drone_coords[0] - DRONE_IMG_WIDTH/2, drone_coords[1] - DRONE_IMG_WIDTH/2)
    surface.blit(drone_img, image_coords)
    pygame.draw.circle(surface, DRONE_SEARCH_RADIUS_COLOR, drone.returnCoords(), drone.getSearchRadius(), 1)

def draw_drone_path(drone):
    points = drone.get_location_history()
    if len(points) < 2:
        return
    pygame.draw.aalines(surface, DRONE_PATH_COLOR, False, points)

def draw_drone_visibility_path(drone):
    points = drone.get_location_history()
    if len(points) < 2:
        return
    for p in points:
        pygame.draw.circle(surface, DRONE_VISIBILITY_PATH_COLOR, p, drone.getSearchRadius(), 0)

def render(person_list, drone_list):
    surface.fill(OCEAN)

    # needs to be drawn before the drones so it doesn't draw on top of them
    for drone in drone_list:
        draw_drone_visibility_path(drone)
    for drone in drone_list:
        draw_drone_path(drone)
    for drone in drone_list:
        draw_drone(drone)

    for person in person_list:
        draw_person(person)

    screen.blit(surface, (0,0))

    pygame.display.update()
    fps.tick(30)



if __name__ == "__main__":

    bck = backend.Backend(ALG_TO_USE, NUM_DRONES, NUM_PEOPLE, SIZE[0], SIZE[1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        world_state = bck.update()
        render(world_state.peopleList, world_state.droneList)
