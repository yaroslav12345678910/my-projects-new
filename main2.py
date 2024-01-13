import pygame

# Initialize pygame and create a window
pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Window")

# Create a font and a text surface to display the number of times the window was minimized
font = pygame.font.Font(None, 100)
text_surface = font.render("0", True, (255, 0, 0))

# Create a variable to keep track of the number of times the window was minimized
minimized_count = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.ACTIVEEVENT:
            if event.state == pygame.APPACTIVE and event.gain == 0:
                minimized_count += 1
                text_surface = font.render(str(minimized_count), True, (255, 0, 0))

    # Clear the screen
    window.fill((0, 0, 0))

    # Blit the text surface to the center of the screen
    window.blit(text_surface, (50, 50))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()