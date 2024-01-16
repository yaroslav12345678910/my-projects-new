import pygame

pygame.init()
size = width, height = 1200, 675
sc = pygame.display.set_mode(size)
FPS = 60
clock = pygame.time.Clock()
player_icon = pygame.image.load("player.png")
player_x = 650
player_y = 500
BLACK = (0, 0, 0)
speed = 13
background_image = pygame.image.load("volcanoes.jpg")

isJump = False
jumpCount = 10
flag_space = True
running = True

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sc.blit(background_image, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            player_y -= (jumpCount * abs(jumpCount)) * 0.7
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    sc.blit(player_icon, (player_x, player_y))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
