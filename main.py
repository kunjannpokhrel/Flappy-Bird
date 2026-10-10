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


MENU = "menu"
CHARACTERS ="characters"
BACKGROUNDS = "backgrounds"
SETTINGS ="settings"
PLAYING = "playing"
state=MENU

TITLE_FONT=pygame.font.SysFont("arial", 44, bold=True)
FONT=pygame.font.SysFont("arial", 23, bold=True)
SMALL_FONT= pygame.font.SysFont("arial", 16)

running=True
while running:

    if state==CHARACTERS:

        # Background
        background.draw(screen)
        ground.draw(screen)

        # Title
        title = TITLE_FONT.render("CHARACTERS", True, WHITE)
        screen.blit(title, title.get_rect(center=(400, 80)))

        subtitle = SMALL_FONT.render("CHOOSE YOUR CHARACTER", True, "CYAN")
        screen.blit(subtitle, subtitle.get_rect(center=(400, 125)))

        # Back button
        back_button = pygame.Rect(30, 30, 100, 40)
        pygame.draw.rect(screen, BLUE, back_button, border_radius=10)
        back_text = FONT.render("BACK", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        # Character rectangles
        character1 = pygame.Rect(130, 180, 150, 120)
        character2 = pygame.Rect(325, 180, 150, 120)
        character3 = pygame.Rect(520, 180, 150, 120)
        character4 = pygame.Rect(130, 350, 150, 120)
        character5 = pygame.Rect(325, 350, 150, 120)
        character6 = pygame.Rect(520, 350, 150, 120)

        # Draw characters
        pygame.draw.rect(screen, (255, 100, 100), character1, border_radius=10)
        pygame.draw.rect(screen, (255, 170, 65), character2, border_radius=10)
        pygame.draw.rect(screen, (255, 225, 80), character3, border_radius=10)
        pygame.draw.rect(screen, (75, 200, 125), character4, border_radius=10)
        pygame.draw.rect(screen, (75, 155, 255), character5, border_radius=10)
        pygame.draw.rect(screen, (185, 115, 255), character6, border_radius=10)


    if state==BACKGROUNDS:
        # Back button
        back_button = pygame.Rect(30, 30, 100, 40)
        pygame.draw.rect(screen, BLUE, back_button, border_radius=10)
        back_text = FONT.render("BACK", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

    if state==SETTINGS:
        # Back button
        back_button = pygame.Rect(30, 30, 100, 40)
        pygame.draw.rect(screen, BLUE, back_button, border_radius=10)
        back_text = FONT.render("BACK", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

    if state==MENU: 

        # Main menu buttons
        play_button =pygame.Rect(275, 200, 250, 50)
        characters_button =pygame.Rect(275, 265, 250, 50)
        backgrounds_button =pygame.Rect(275, 330, 250, 50)
        settings_button =pygame.Rect(275, 395, 250, 50)
        quit_button =pygame.Rect(275, 460, 250, 50)

        # Background
        background.draw(screen)
        ground.draw(screen)

        # Title
        title =TITLE_FONT.render("FLAPPY BIRD", True, WHITE)
        screen.blit(title, title.get_rect(center=(400, 100)))

        subtitle =SMALL_FONT.render("MAIN MENU", True, "Black")
        screen.blit(subtitle, subtitle.get_rect(center=(400, 150)))

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

        
            
    if state==PLAYING :
        background.draw(screen)
        ground.draw(screen)
        bird.draw(screen)
        # Back button
        back_button = pygame.Rect(30, 30, 100, 40)
        pygame.draw.rect(screen, BLUE, back_button, border_radius=10)
        back_text = FONT.render("BACK", True, WHITE)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            running=False

        elif keys[pygame.K_F11] or keys[pygame.K_f]:
            pygame.display.toggle_fullscreen() 

        elif event.type == pygame.MOUSEBUTTONDOWN:
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
            elif back_button.collidepoint(event.pos):
                state = MENU
            elif character1.collidepoint(event.pos):
                selected_character = 1
            elif character2.collidepoint(event.pos):
                selected_character = 2
            elif character3.collidepoint(event.pos):
                selected_character = 3
            elif character4.collidepoint(event.pos):
                selected_character = 4
            elif character5.collidepoint(event.pos):
                selected_character = 5
            elif character6.collidepoint(event.pos):
                selected_character = 6

    pygame.display.flip()
    clock.tick(60)
pygame.quit()