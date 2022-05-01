import pygame
import numpy as np
class Particle:
    def __init__(self, pos, v=0, a=0, mass=1):
        self.pos = pos
        self.v = v
        self.a = a
        self.mass = mass
        self.clicked = False


    def apply_force(self, force):
        f = force / self.mass
        self.a += f


    def show(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos[0], self.pos[1]), radius=5)


    def update(self):
        if(not self.clicked):
            self.v *= .99
            self.v += self.a
            self.pos += self.v
            self.a = 0
            self.v -= np.array([0, -9.8])*.001