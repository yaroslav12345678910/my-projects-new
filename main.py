import pygame

pygame.init()
pygame.font.init()
count = 1
size = width, height = 200, 200
sc = pygame.display.set_mode(size)
f1 = pygame.font.Font(None, 100)
text1 = f1.render(str(count), True,
                              (255, 0, 0))
sc.blit(text1, (85, 60))
pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.WINDOWHIDDEN:
            count += 1
            text1 = f1.render(str(count), True,
                              (255, 0, 0))
            sc.blit(text1, (85, 60))
            pygame.display.update()