import pygame
import pygamegui

pygame.init()

pygame.display.set_caption('Start')
window_surface = pygame.display.set_mode((800, 800))

background = pygame.Surface((800, 600))

background.fill(pygame.Color("#FFFFFF"))

manager = pygamegui.UIManager((800, 600))

clock = pygame.time.Clock()

run = True
while run:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        mana
    window_surface.blit(background, (0, 0))

    pygame.display.update()
