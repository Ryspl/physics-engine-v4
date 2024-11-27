#physics project sim V4

#main loop
import pygame
import Vector2
import shapes
import RigidBody

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
























while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")






    pygame.display.flip()

    clock.tick(120)

pygame.quit()