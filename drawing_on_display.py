import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGTH = 600 
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Drawing Objects")

# Define colors are RGB tuples
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# Give a background color to the window
display_surface.fill(BLUE)

# Draw various shapes in our display
# Line(surface, color, starting_point, ending_point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100),5)
pygame.draw.line(display_surface, GREEN, (100,100),(200,300),1)

# Circle(surface, color, center, radius, thickness )
pygame.draw.circle(display_surface, WHITE,(WINDOW_WIDTH//2,WINDOW_HEIGTH//2), 200, 6 )


# The game main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the display
    pygame.display.update()
# End game
pygame.quit()
