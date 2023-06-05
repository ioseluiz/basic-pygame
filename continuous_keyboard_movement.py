import pygame

# Initialize pygame
pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGTH = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Continuous Keyboard Movement")

# Set game vales
VELOCITY = 5


# Load images
dragon_image = pygame.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2,WINDOW_HEIGTH//2)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Get a list of all keys currently being pressend down
    keys = pygame.key.get_pressed()
    print(keys)
    
    # Move the dragon continuously
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY
            
    # Fill the display surface to cover old images
    display_surface.fill((0,0,0))
    
    # Blit (copy) images to the screen
    display_surface.blit(dragon_image, dragon_rect)
    
    # Update the display
    pygame.display.update()
            
# End game
pygame.quit()