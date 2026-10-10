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
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            running=False
        if keys[pygame.K_F11] or keys[pygame.K_f]:
            pygame.display.toggle_fullscreen() 

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

    pygame.display.flip()
    clock.tick(60)
pygame.quit()