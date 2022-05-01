from cmath import pi
import numpy as np
import spring
import particle
import pygame

background_colour = (12,12,12)
screen = pygame.display.set_mode((800,1200))
pygame.display.set_caption("Wire")
screen.fill(background_colour)
pygame.display.flip()
running = True


particles = []
springs = []

for i in range(50):
    p = particle.Particle(np.array([100.0 + (i*10),100.0 + (i*10)]))
    particles.append(p)
    if i >= 1:
        s = spring.Spring(.1, particles[i], particles[i-1], 1)
        springs.append(s)


while running:
    screen.fill(background_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for s in springs:
        s.update()
        s.show(screen)

    for p in particles:
        p.update()
        p.show(screen)
        if p == particles[-1] and pygame.mouse.get_pressed()[0]:
            p.clicked = True
            p.pos = pygame.mouse.get_pos()
            p.v = np.array([0.,0.])
        else :
            p.clicked = False

    pygame.display.flip()
    pygame.display.update()