import pygame
import numpy as np
class Particle:
    # Constructor
    def __init__(self, pos, v=0, a=0, mass=1):
        self.pos = pos
        self.v = v
        self.a = a
        self.mass = mass
        self.clicked = False


    #to string method
    def __str__(self):
        return "Particle: " + str(self.pos) + " " + str(self.v) + " " + str(self.a) + " " + str(self.mass)


    #adds force to the particle
    def apply_force(self, force):
        f = force / self.mass                   #f = ma
        self.a += f                             #a = a + f/m


    #Draw the particle on the screen.
    def show(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos[0], self.pos[1]), radius=5)


    #Update the particle's position and velocity based on the acceleration.
    def update(self):
        if(not self.clicked):                   # if the particle is not clicked
            self.v *= .99                       # make the velocity slower
            self.v += self.a                    # add the acceleration to the velocity
            self.pos += self.v                  # add the velocity to the position
            self.a = 0                          # reset acceleration
            self.v -= np.array([0, -9.8])*.001  # adds gravity to the particle

        
    #Getters and setters for the particle's variables.
    def getPos(self): 
        return self.pos

    def getV(self):
        return self.v

    def getA(self):
        return self.a

    def getMass(self):
        return self.mass

    def getClicked(self):
        return self.clicked

    def setPos(self, pos):
        self.pos = pos

    def setV(self, v):
        self.v = v

    def setA(self, a):
        self.a = a

    def setMass(self, mass):
        self.mass = mass

    def setClicked(self, clicked):
        self.clicked = clicked