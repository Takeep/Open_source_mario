import pygame

pygame.init()

pygame.display.set_mode((500, 500))


def quitgame():
    done = False

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                done = True

        pygame.display.flip()


quitgame()
