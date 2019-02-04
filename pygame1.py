import pygame
import random
# import cx_Freeze

"""BUGS!!
elbocoins: inside blue boxes
            not always counting
crashed: Not an under car y-axis,
                this makes the car crash in all objects under itself"""

# !!Must have!!
pygame.init()

crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("jazz.mp3")

# Screensize
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)
blue_gr = (53, 115, 255)

car_width = 92

pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racerbil.png')
carIco = pygame.image.load('racericon.png')
elBo = pygame.image.load('electroboom.png')


pygame.display.set_icon(carIco)


def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Fedme: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def elbocoin(coins):
    coins += 1
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Electrobooms: " + str(coins - 1), True, blue)
    gameDisplay.blit(text, (500, 0))
    return coins


def electroboom(elx, ely):
    gameDisplay.blit(elBo, (elx, ely))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# def message_display(text):
#     largeText = pygame.font.SysFont("comicsansms", 40)
#     TextSurf, TextRectangle = text_objects(text, largeText)
#     TextRectangle.center = ((display_width / 2), (display_height / 2))
#     gameDisplay.blit(TextSurf, TextRectangle)
#     pygame.display.update()
#     time.sleep(2)

#     game_loop()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    # gameDisplay.fill(white)

    largeText = pygame.font.SysFont("comicsansms", 40)
    TextSurf, TextRectangle = text_objects("Du kræsja fordi du har høy fedme%", largeText)
    TextRectangle.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        button("Play Again", 150, 450, 150, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, inact_c, act_c, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Hover buttons
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, act_c, (x, y, w, h))
        if click[0] == 1 and action is not None:
            # //Kjører funksjonen som er i variabelen active
            action()
    else:
        pygame.draw.rect(gameDisplay, inact_c, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 30)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), y + (h / 2))
    gameDisplay.blit(TextSurf, TextRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRectangle = text_objects("Paused", largeText)
    TextRectangle.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRectangle)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        button("Continue", 150, 450, 150, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 100)
        TextSurf, TextRectangle = text_objects("A bit Racey", largeText)
        TextRectangle.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRectangle)

        button("Go!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():

    global pause
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0

    # Thing=Bokser man krasjer i
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - int(thing_width))
    thing_starty = -600

    # Electrobooms
    elspeed = 7
    elstartx = random.randrange(0, display_width - int(50))
    elstarty = -3000

    dodged = 0
    elbocoins = 0
    maxelbocoins = 1

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color, nr)
        things(thing_startx, thing_starty, thing_width, thing_height, blue_gr)

        thing_starty += thing_speed

        electroboom(elstartx, elstarty)

        elstarty += elspeed

        car(x, y)
        things_dodged(dodged)
        elbocoin(elbocoins)

        # Crashing
        if x > display_width - car_width or x < 0:
            crash()

        # Block kommer til bunn
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - int(thing_width))
            dodged += 1
            if thing_width < (display_width / 4):
                thing_width += (dodged * 1.2)

        if elstarty > display_height:
            elstarty = random.randrange(-5000, -500)
            elstartx = random.randrange(0, display_width - 50)
            if catched_coin:
                maxelbocoins += 1

        catched_coin = False

        # Hvis boksen passerer bilens y-akse
        if y < thing_starty + thing_height:
            # Hvis blien er innenfor boksens "to" x-akser
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        if y < elstarty + 50:
            if x > elstartx and x < elstartx + 50 or x + 50 > elstartx and x + 50 < elstartx + 50:
                catched_coin = True
                # Bare en elbocoin
                while elbocoins < maxelbocoins:
                    elbocoins = elbocoin(elbocoins)

        # Kan ta parameters for å oppdatere bare spesifike ting
        pygame.display.update()

        clock.tick(60)


game_intro()
game_loop()
quitgame()
