import pygame
import particle
import numpy as np

class Spring:
    def __init__(self, k, pA, pB, rest_length):
        self.k = k*.001
        self.particle = particle
        self.pA = pA
        self.pB = pB
        self.rest_length = rest_length

    def update(self):
        force = self.pB.pos - self.pA.pos
        length = np.linalg.norm(force) - self.rest_length
        force *= self.k * length
        self.pA.apply_force(force)
        self.pB.apply_force(-force)

    def show(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.pA.pos, self.pB.pos, 1)

  
