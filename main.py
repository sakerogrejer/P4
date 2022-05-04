'''
DEVELOPER: Isak Vennard
DATE: 5/3/2022
'''

"""Soft body and string/wire simulation.

Using the ideas of springs and particles, create a wire that can be
dragged around the screen. The wire should be able to be stretched and
compressed. The wire should also be able to bend.
"""


import numpy as np
import spring
import particle
import pygame

#Main function
def main():   
    
    #Setup the screen and text
    background_colour = (12,12,12)
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Wire")
    screen.fill(background_colour)
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.Font("font.ttf", 70)
    textl = font.render("L-MB DRAG BOTTOM", True, (255,255,255))
    textr = font.render("R-MB DRAG TOP", True, (255,255,255))
    text_rect = textl.get_rect()
    text_rect.topright = (700, 0)
    text_rect2 = textr.get_rect()
    text_rect2.topright = (685, 70)
    running = True

    #Setup the particles
    particles = []
    springs = []

    #Setup the spring, connect a sprint from each particle to the next one
    for i in range(36):
        p = particle.Particle(np.array([100.0 + i*10,100.0 + i*10]), .1)
        particles.append(p)
        if i >= 1:
            s = spring.Spring(2, particles[i], particles[i-1], 2, True)
            springs.append(s)


    #Main loop
    while running:

        #Draw text and background
        screen.fill(background_colour)
        screen.blit(textl, text_rect)
        screen.blit(textr, text_rect2)
        
        #Stop game if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Update the particles and springs
        for s in springs:
            s.update()
            s.show(screen)

        for p in particles:
            p.update()
            p.show(screen)

            #Cap the velocity of the particles
            if(p.v[0] > 1000):
                p.v[0] = 1000
            if(p.v[1] > 1000):
                p.v[1] = 1000

            #Set the bottom particle to the mouse position
            if p == particles[-1] and pygame.mouse.get_pressed()[0]:
                p.clicked = True
                p.v = np.array([0.,0.])
                p.a = np.array([0.,0.])
                p.pos += (pygame.mouse.get_pos() - p.pos)*.1
                
            #Set the top particle to the mouse position and keep the position fixed after the mouse is released
            if p == particles[0]:
                if pygame.mouse.get_pressed()[2]:
                    p.clicked = True
                    p.v = np.array([0.,0.])
                    p.a = np.array([0.,0.])
                    p.pos += (pygame.mouse.get_pos() - p.pos)*.1
                else:
                    p.clicked = True
                    p.v = np.array([0.,0.])
                    p.a = np.array([0.,0.])
            else:
                p.clicked = False

        #orient the display
        pygame.display.flip()
        pygame.display.update()


#Run the main function
if __name__ == "__main__":
    main()