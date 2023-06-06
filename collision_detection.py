import pygame

# Initialize pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGTH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Collision Detection")

# Set the FPS and clock
FPS = 60
clock = pygame.time.clock()

# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGTH//2)


#Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Fill surface
    display_surface.fill((0,0,0))
    
    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
            

            
# End the game
pygame.quit()