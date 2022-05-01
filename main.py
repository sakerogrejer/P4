from cmath import pi
import numpy as np
import spring
import pygame

background_colour = (12,12,12)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Wire")
screen.fill(background_colour)
pygame.display.flip()
running = True
 
s = spring.Spring(.001, np.array([[350.0, 250.0],[400.0, 300.0]]), 100, damping=.999)
while running:
    screen.fill(background_colour)
    s.draw(screen)
    s.update()

    if pygame.mouse.get_pressed()[0]:
        s.pos[1] = np.array([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
        s.v = np.array([0.0, 0.0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.display.update()