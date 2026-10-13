import pygame
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,600) ,pygame.FULLSCREEN| pygame.SCALED)
pygame.display.set_caption("FLAPPY BIRD")

from classes import Background, Ground, Bird
clock=pygame.time.Clock()

background=Background()
ground=Ground()
bird=Bird()

# Colors
WHITE =(255, 255, 255)
BLACK =(25, 30, 45)
BLUE =(65, 130, 210)
SKY_BLUE =(135, 206, 235)
GREEN =(100, 200, 120)
YELLOW=(255, 220, 90)
GREY =(180, 190, 205)
DARK = (25, 32, 50)
RED=(255,0,0)


MENU = "menu"
CHARACTERS ="characters"
BACKGROUNDS = "backgrounds"
SETTINGS ="settings"
PLAYING = "playing"
state=MENU

TITLE_FONT=pygame.font.SysFont("arial", 44, bold=True)
FONT=pygame.font.SysFont("arial", 23, bold=True)
SMALL_FONT= pygame.font.SysFont("arial",16)

back_button = pygame.Rect(30, 30, 100, 40)
selected_character=1
# character loads
character_images = []
for i in range(6):
    img = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-midflap.png").convert()
    img = pygame.transform.scale(img, (150, 120))
    character_images.append(img)

character_rects = [pygame.Rect(130, 180, 150, 120),pygame.Rect(325, 180, 150, 120),
                   pygame.Rect(520, 180, 150, 120),pygame.Rect(130, 350, 150, 120),
                   pygame.Rect(325, 350, 150, 120),pygame.Rect(520, 350, 150, 120)]

# background loads
background_images = []
for i in range(6):
    img = pygame.image.load("assets\\Game Objects\\background-day.png").convert()
    img = pygame.transform.scale(img, (150, 120))
    background_images.append(img)

background_rects = [pygame.Rect(130, 180, 150, 120),pygame.Rect(325, 180, 150, 120),
                   pygame.Rect(520, 180, 150, 120),pygame.Rect(130, 350, 150, 120),
                   pygame.Rect(325, 350, 150, 120),pygame.Rect(520, 350, 150, 120)]

selected_background = 0 
selected_background = 0 

def headline_menu():
    title =TITLE_FONT.render("FLAPPY BIRD", True, WHITE)
    screen.blit(title, title.get_rect(center=(400, 100)))

    subtitle =SMALL_FONT.render("MAIN MENU", True, "Black")
    screen.blit(subtitle, subtitle.get_rect(center=(400, 150)))

def headline_text(topic):
        title = TITLE_FONT.render(f"{topic}S", True, WHITE)
        screen.blit(title, title.get_rect(center=(400, 80)))

        subtitle = SMALL_FONT.render(f"CHOOSE YOUR {topic}", True, "CYAN")
        screen.blit(subtitle, subtitle.get_rect(center=(400, 125)))

def backbutton():
        pygame.draw.rect(screen, BLUE, back_button, border_radius=10)
        back_text = FONT.render("BACK", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

def menubuttons():
    # Buttons
    pygame.draw.rect(screen, BLUE, play_button, border_radius=12)
    pygame.draw.rect(screen, BLUE, characters_button, border_radius=12)
    pygame.draw.rect(screen, BLUE, backgrounds_button, border_radius=12)
    pygame.draw.rect(screen, BLUE, settings_button, border_radius=12)
    pygame.draw.rect(screen, BLUE, quit_button, border_radius=12)

    # Button text
    play_text =FONT.render("PLAY", True, WHITE)
    characters_text =FONT.render("CHARACTERS", True, WHITE)
    backgrounds_text =FONT.render("BACKGROUNDS", True, WHITE)
    settings_text = FONT.render("SETTINGS", True, WHITE)
    quit_text =FONT.render("QUIT", True, WHITE)

    screen.blit(play_text, play_text.get_rect(center=play_button.center))
    screen.blit(characters_text, characters_text.get_rect(center=characters_button.center))
    screen.blit(backgrounds_text, backgrounds_text.get_rect(center=backgrounds_button.center))
    screen.blit(settings_text, settings_text.get_rect(center=settings_button.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_button.center)) 


    
running=True
while running:

    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            running=False

        elif keys[pygame.K_F11] or keys[pygame.K_f]:
            pygame.display.toggle_fullscreen() 

        if event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:
          if back_button.collidepoint(event.pos):
            state = MENU

    if state==PLAYING:
        background.draw(screen)
        ground.draw(screen)
        bird.draw(screen)
        backbutton()



    if state==CHARACTERS:

        # Background
        background.draw(screen)
        ground.draw(screen)
        headline_text(topic="CHARACTER")
        backbutton()

        for i in range(0,6):
            screen.blit(character_images[i], character_rects[i])
            if selected_character == i+1:
                border_color = RED 
            else:
                border_color=DARK
            pygame.draw.rect(screen, border_color, character_rects[i], 3)
            

    if state==BACKGROUNDS:
        background.draw(screen)
        ground.draw(screen)
        headline_text(topic="BACKGROUND")
        backbutton()

        for i in range(0,6):
            screen.blit(background_images[i], background_rects[i])
            if selected_background == i+1:
                border_color = RED 
            else:
                border_color=DARK
            pygame.draw.rect(screen, border_color, character_rects[i], 3)


    if state==SETTINGS:
        backbutton()


    if state==MENU:
        backbutton() 

        # Main menu buttons
        play_button =pygame.Rect(275, 200, 250, 50)
        characters_button =pygame.Rect(275, 265, 250, 50)
        backgrounds_button =pygame.Rect(275, 330, 250, 50)
        settings_button =pygame.Rect(275, 395, 250, 50)
        quit_button =pygame.Rect(275, 460, 250, 50)

        # Background
        background.draw(screen)
        ground.draw(screen)
        headline_menu()
        menubuttons()

        if event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:
            if play_button.collidepoint(event.pos):
                state=PLAYING
            elif characters_button.collidepoint(event.pos):
                state=CHARACTERS
            elif backgrounds_button.collidepoint(event.pos):
                state=BACKGROUNDS
            elif settings_button.collidepoint(event.pos):
                state=SETTINGS
            elif quit_button.collidepoint(event.pos):
                running=False


    pygame.display.flip()
    clock.tick(60)
pygame.quit()