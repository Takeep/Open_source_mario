import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
x=60
y=60

done = False

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
