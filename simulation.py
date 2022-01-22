import pygame
import sys

import backend

SIZE = width, height = 500,500

# person_position = []
# drone_positions = [[x, y], ...]



# speed = [1,1]

# OCEAN = (0,0,255)

# pygame.init()
# screen = pygame.display.set_mode(SIZE)
# fps = pygame.time.Clock()

# person_pos = [50, 50]
# move_counter = 0

# def render():
#   screen.fill(OCEAN)
#   pygame.draw.circle(screen, (0,0,0), person_pos, 5, 0)
#   pygame.display.update()
#   fps.tick(60)



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
  x = backend.UpdateAttrs()
  print(x.person_pos)
