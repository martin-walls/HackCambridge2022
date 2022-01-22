import pygame
import sys

import backend

SIZE = width, height = 700,500

# COLORS
OCEAN = (0,0,255)
BLACK = (0,0,0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)
fps = pygame.time.Clock()


def draw_person(pos):
  pygame.draw.circle(screen, BLACK, pos, 5, 0)

def draw_drone(pos):
  pygame.draw.circle(screen, WHITE, pos, 3, 0)

def render(person_pos, drone_pos):
  screen.fill(OCEAN)
  draw_person(person_pos)
  for drone in drone_pos:
    draw_drone(drone)
  pygame.display.update()
  fps.tick(60)




if __name__ == "__main__":

  while True:
    attrs = backend.update()
    render(attrs.person_pos, attrs.drone_positions)
