import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))

gameDisplay.fill(black)

# Lage pixsler
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

# Lage linjer
# (display, farge, start, slutt, tykkelse)
pygame.draw.line(gameDisplay, blue, (100, 200), (300, 500), 5)

# Lage firkanter
# (display, farge, (startØversteHøyreHjørne, bredde, høyde))
pygame.draw.rect(gameDisplay, red, (400, 400, 70, 35))

# Lage Sirlkler
# (display, farge, senter, radius)
pygame.draw.circle(gameDisplay, white, (500, 500), 30)

# Lage mangekanter
# (display, farge, (koordinater))
pygame.draw.polygon(gameDisplay, green, ((625, 75), (90, 125), (400, 500), (300, 280), (600, 470), (400, 200)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
