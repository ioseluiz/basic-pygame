import pygame

# Initialize pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGTH = 300

surface_display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Mouse Movements")

# Set the game values
VELOCITY = 30

# Load images
dragon_image = pygame.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)



# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Move based on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
            
        # Drag the object whe the mouse button is clicked
            
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
            
            
            
    # Fill the display
    surface_display.fill((0,0,0))
    
    # Blit assets
    surface_display.blit(dragon_image, dragon_rect)
    
    # Update the display
    pygame.display.update()
            
            
# End game
pygame.quit()