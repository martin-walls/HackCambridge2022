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


# speed = [1,1]


# pygame.init()

# person_pos = [50, 50]
# move_counter = 0

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



# while True:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()

#   person_position, drone_positions = backend.update()

#   move_counter += 1

#   if (move_counter == 20):
#     person_pos[0] += 1
#     move_counter = 0

#   render()

if __name__ == "__main__":

  while True:
    render((50, 50), [(30, 100), (200, 150), (300, 400)])

  # x = backend.UpdateAttrs()
  # print(x.person_pos)
