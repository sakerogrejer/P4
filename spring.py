import pygame
import particle
import numpy as np


class Spring:
    
    # Constructor
    def __init__(self, k, pA, pB, rest_length, draw):
        self.k = k*.001                                   #k = k*10^-3 (scalar) (k is in Newtons/meter)
        self.particle = particle                          # 
        self.pA = pA                                      #
        self.pB = pB                                      #
        self.rest_length = rest_length                    #distance that the spring wants to be from the particles
        self.draw = draw


    # Update the spring position and velocity based on the particles.
    def update(self):
        force = self.pB.pos - self.pA.pos                 #force = pB - pA (vector)
        length = np.linalg.norm(force) - self.rest_length #length = |force| - rest_length (scalar)
        force *= self.k * length                          #force = k*length (vector)
        self.pA.apply_force(force)                        #force =  force (vector)
        self.pB.apply_force(-force)                       #force = -force (vector)

    # Draw the spring if it is set to draw.
    def show(self, screen):
        if self.draw:
            pygame.draw.line(screen, (255, 255, 255), self.pA.pos, self.pB.pos, 2)
        else:
            pass

    # Print the spring's information.
    def __str__(self):
        return "Spring" + str(self.k) + " " + str(self.pA) + " " + str(self.pB) + " " + str(self.rest_length)

    #Getters and setters for the spring's variables.
    def getK(self):
        return self.k
    
    def getPA(self):
        return self.pA

    def getPB(self):
        return self.pB

    def getRestLength(self):
        return self.rest_length

    def getDraw(self):
        return self.draw

    def setK(self, k):
        self.k = k

    def setPA(self, pA):
        self.pA = pA

    def setPB(self, pB):
        self.pB = pB

    def setRestLength(self, rest_length):
        self.rest_length = rest_length

    def setDraw(self, draw):
        self.draw = draw

    

  
