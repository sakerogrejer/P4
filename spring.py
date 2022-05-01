import pygame
import numpy as np

class Spring:
    def __init__(self, k, pos, rest_length, v=0, a=0, damping=.999):
        self.k = k*.001
        self.pos = pos
        self.rest_length = rest_length
        self.v = v
        self.a = a
        self.damping = damping


    def __str__(self):
        return f"Spring(k={self.k}, y={self.pos}, rest_length={self.rest_length}, v={self.v}, a={self.a})"


    def get_force(self):
        v = self.pos[1] - self.pos[0]
        x = np.linalg.norm(v) - self.rest_length
        return v * (-1 * self.k * x)


    def update(self):
        self.a = self.get_force()
        self.v += self.a
        self.v -= np.array([0.0, -0.00981])
        #self.pos[0] -= self.v
        self.pos[1] += self.v
        self.v *= self.damping


    def draw(self, screen):
        pygame.draw.line(screen, (255,255,255), self.pos[0], self.pos[1], 1)
        pygame.draw.circle(screen, (255, 0, 0), (self.pos[1][0], self.pos[1][1]), radius=5)
        pygame.draw.circle(screen, (0, 0, 255), (self.pos[0][0], self.pos[0][1]), radius=5)


