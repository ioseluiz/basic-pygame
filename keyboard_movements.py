import pygame

# Initialize pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 300


display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption("Discrete Movements")

# Set the games vales
VELOCITY = 10

# Load in images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = SCREEN_WIDTH//2
dragon_rect.bottom = SCREEN_HEIGTH

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY
                
    # Fill the display surface to cover old images
    display_surface.fill((0,0,0))
            
    # Blit (copy) the assets to the screen
    display_surface.blit(dragon_image, dragon_rect)
    
    # Update the display
    pygame.display.update()
            
# End the game            
pygame.quit()