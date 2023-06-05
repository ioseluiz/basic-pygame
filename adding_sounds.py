import pygame

# Initialize pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 300


display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption("Adding Sounds!")


# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
# End the game            
pygame.quit()