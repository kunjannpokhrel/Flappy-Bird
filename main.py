import pygame
import webbrowser
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,600) ,pygame.FULLSCREEN| pygame.SCALED)
pygame.display.set_caption("FLAPPY BIRD")

from classes import Background, Ground, Bird,Click,Pipe,Wing
clock=pygame.time.Clock()

ground=Ground()
bird=Bird()
click=Click()
pipe=Pipe()
wing=Wing()

background_list=[]
for i in range(6):
   background_list.append(Background(i))


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
ABOUT ="ABOUT"
PLAYING = "playing"
READY="ready"
GAMEOVER="GAMEOVER"
state=MENU
score = 0

TITLE_FONT=pygame.font.SysFont("arial", 44, bold=True)
FONT=pygame.font.SysFont("arial", 23, bold=True)
SMALL_FONT= pygame.font.SysFont("arial",16)

back_button = pygame.Rect(30, 30, 100, 40)
start_game_button=pygame.Rect(275, 350, 250, 50) 
menu_button=pygame.Rect(275, 380, 250, 50)     
selected_character=1

# character loads
character_images = []
for i in range(6):
    img = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-midflap.png").convert()
    img = pygame.transform.scale(img, (110, 80))
    character_images.append(img)

character_rects = [pygame.Rect(130, 180, 150, 120),pygame.Rect(325, 180, 150, 120),
                   pygame.Rect(520, 180, 150, 120),pygame.Rect(130, 350, 150, 120),
                   pygame.Rect(325, 350, 150, 120),pygame.Rect(520, 350, 150, 120)]

# background loads
background_images = []
for i in range(6):
    img = pygame.image.load(f"assets\\Background\\background{i}.png").convert()
    img = pygame.transform.scale(img, (150, 120))
    background_images.append(img)

background_rects = [pygame.Rect(130, 180, 150, 120),pygame.Rect(325, 180, 150, 120),
                   pygame.Rect(520, 180, 150, 120),pygame.Rect(130, 350, 150, 120),
                   pygame.Rect(325, 350, 150, 120),pygame.Rect(520, 350, 150, 120)]

selected_background = 1

# Main menu buttons
play_button =pygame.Rect(275,200,250, 50)
characters_button =pygame.Rect(275, 265,250, 50)
backgrounds_button =pygame.Rect(275,330, 250, 50)
ABOUT_button =pygame.Rect(275, 395,250, 50)
quit_button =pygame.Rect(275,460,250, 50)

github_button = pygame.Rect(200, 420, 400, 40)
linkedin_button = pygame.Rect(200, 480, 400, 40)

def headline_menu():

    title = TITLE_FONT.render("FLAPPY BIRD", True, WHITE)
    screen.blit(TITLE_FONT.render("FLAPPY BIRD", True, BLACK), title.get_rect(center=(402, 102)))
    screen.blit(title, title.get_rect(center=(400, 100)))

    subtitle =SMALL_FONT.render("MAIN MENU", True, WHITE)
    screen.blit(subtitle, subtitle.get_rect(center=(400, 150)))

def headline_text(topic):
        title = TITLE_FONT.render(f"{topic}S", True, WHITE)
        screen.blit(TITLE_FONT.render(f"{topic}S", True, BLACK), title.get_rect(center=(402, 82)))
        screen.blit(title, title.get_rect(center=(400, 80)))

        subtitle = SMALL_FONT.render(f"CHOOSE YOUR {topic}", True, DARK)
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
    pygame.draw.rect(screen, BLUE, ABOUT_button, border_radius=12)
    pygame.draw.rect(screen, BLUE, quit_button, border_radius=12)

    # Button text
    play_text =FONT.render("PLAY", True, WHITE)
    characters_text =FONT.render("CHARACTERS", True, WHITE)
    backgrounds_text =FONT.render("BACKGROUNDS", True, WHITE)
    ABOUT_text = FONT.render("ABOUT", True, WHITE)
    quit_text =FONT.render("QUIT", True, WHITE)

    screen.blit(play_text, play_text.get_rect(center=play_button.center))
    screen.blit(characters_text, characters_text.get_rect(center=characters_button.center))
    screen.blit(backgrounds_text, backgrounds_text.get_rect(center=backgrounds_button.center))
    screen.blit(ABOUT_text, ABOUT_text.get_rect(center=ABOUT_button.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_button.center)) 

def draw_background():
 bg_index= selected_background - 1
 background_list[bg_index].draw(screen)

def reset():
    global bird ,pipe, ground ,score ,state
    bird= Bird()      
    pipe= Pipe()     
    ground= Ground()  
    score=0          
    state= MENU   

running=True
while running:
    draw_background()

    if state in [READY,PLAYING,GAMEOVER]:
        pipe.draw(screen)
        ground.draw(screen)
        bird.draw(screen)


    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            running=False
 
        elif event.type == pygame.KEYDOWN:
            if state == PLAYING:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.space()
                    wing.play()
            elif state == READY:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    state = PLAYING
                    bird.space()
                    wing.play()

            elif keys[pygame.K_F11] or keys[pygame.K_f]:
                pygame.display.toggle_fullscreen() 

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if state not in [MENU,READY,GAMEOVER] and back_button.collidepoint(event.pos):
                state = MENU
                click.play()

            elif state == MENU:
                if play_button.collidepoint(event.pos):
                    state = READY 
                    click.play()
                elif characters_button.collidepoint(event.pos):
                    state = CHARACTERS
                    click.play()
                elif backgrounds_button.collidepoint(event.pos):
                    state = BACKGROUNDS
                    click.play()
                elif ABOUT_button.collidepoint(event.pos):
                    state = ABOUT
                    click.play()
                elif quit_button.collidepoint(event.pos):
                    running = False
                    click.play()

            elif state== READY:
                if start_game_button.collidepoint(event.pos):
                    state= PLAYING
                    bird.space()
                    wing.play()
            elif state == GAMEOVER:
                if menu_button.collidepoint(event.pos):
                    reset()
                    click.play()
            elif state == CHARACTERS:
                for i in range(6):
                    if character_rects[i].collidepoint(event.pos):
                        selected_character = i + 1
                        click.play()

            elif state == BACKGROUNDS:
                for i in range(6):
                    if background_rects[i].collidepoint(event.pos):
                        selected_background = i + 1
                        click.play()

            elif state == ABOUT:
                if github_button.collidepoint(event.pos):
                    webbrowser.open("https://github.com/kunjannpokhrel")
                    click.play()
                elif linkedin_button.collidepoint(event.pos):
                    webbrowser.open("https://linkedin.com")
                    click.play()

    if state == READY:
        pygame.draw.rect(screen, GREEN,start_game_button, border_radius=12)
        start_text = FONT.render("START GAME", True, WHITE)
        screen.blit(start_text,start_text.get_rect(center=start_game_button.center))
        
        info_text =TITLE_FONT.render("PRESS SPACE TO FLAP & START", True, WHITE)
        screen.blit(info_text,info_text.get_rect(center=(400, 200)))
 

    if state==PLAYING:
        backbutton()
        bird.update()
        pipe.update()
        bird_rect= bird.get_rect()
        all_pipes= pipe.get_rects()
        for pipe_rect in all_pipes:
            if bird_rect.colliderect(pipe_rect):
                state=GAMEOVER
        if bird.y <= 0 or bird.y >= 525:
            state=GAMEOVER
        if pipe.x== 328 or pipe.pipe2_x == 328 or pipe.pipe3_x == 328 or pipe.pipe4_x == 328:
            score += 1

        score_text= FONT.render(f"Score:{score}",True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        bg_index = selected_background - 1
        background_list[bg_index].update() 
        ground.update()

    if state==CHARACTERS:
        headline_text(topic="CHARACTER")
        backbutton()

        for i in range(0,6):
            img_rect = character_images[i].get_rect(center=character_rects[i].center)
            screen.blit(character_images[i], img_rect)
            if selected_character == i+1:
                border_color = RED 
            else:
                border_color=DARK
            pygame.draw.rect(screen, border_color, character_rects[i], 3)

    if state==BACKGROUNDS:
        headline_text(topic="BACKGROUND")
        backbutton()

        for i in range(0,6):
            screen.blit(background_images[i], background_rects[i])
            if selected_background == i+1:
                border_color = RED 
            else:
                border_color=DARK
            pygame.draw.rect(screen, border_color, background_rects[i], 3)

    if state == GAMEOVER:
        go_panel = pygame.Rect(200, 120, 400, 360)
        pygame.draw.rect(screen, DARK,go_panel, border_radius=15)
        
        go_text = TITLE_FONT.render("GAME OVER", True, RED)
        screen.blit(go_text,go_text.get_rect(center=(400, 180)))
        
        final_score_text = FONT.render(f"Final Score: {score}", True, WHITE)
        screen.blit(final_score_text,final_score_text.get_rect(center=(400, 250)))
        
        pygame.draw.rect(screen, BLUE, menu_button, border_radius=12)
        menu_btn_text = FONT.render("MAIN MENU", True, WHITE)
        screen.blit(menu_btn_text,menu_btn_text.get_rect(center=menu_button.center))


    if state==ABOUT:
        backbutton()
    if state == ABOUT:
        headline_text(topic="ABOUT")
        backbutton()

        # 1. ABOUT ME INFOCARD PANEL
        panel_rect = pygame.Rect(100, 150, 600, 390)
        pygame.draw.rect(screen, BLACK, panel_rect, border_radius=15)
        pygame.draw.rect(screen, GREY, panel_rect, width=2, border_radius=15)

        # Biography rendering details
        bio_title = FONT.render("THE DEVELOPER", True, YELLOW)
        screen.blit(bio_title, (130, 175))
        
        bio_p1 = SMALL_FONT.render("Hi lol! myself Kunjan Pokhrel. This is my ", True, WHITE)
        bio_p2 = SMALL_FONT.render("project that i made as my second game hehe.", True, WHITE)
        screen.blit(bio_p1, (130, 210))
        screen.blit(bio_p2, (130, 230))

        pygame.draw.line(screen, DARK, (130, 265), (670, 265), 2)

        ctrl_title = FONT.render("GAME MECHANICS", True, YELLOW)
        screen.blit(ctrl_title, (130, 285))
        
        ctrl_space= SMALL_FONT.render("• SPACEBAR / UP ARROW : Flap wings to fly upward", True, WHITE)
        ctrl_ready= SMALL_FONT.render("• SPACEBAR (On Ready)  : Launch the active bird", True, WHITE)
        ctrl_reset= SMALL_FONT.render("• SPACEBAR (On Death)  : Reset back to Main Menu", True, WHITE)
        ctrl_screen= SMALL_FONT.render("• F11 / F KEY          : Toggle fullscreen window mode", True, WHITE)
        
        screen.blit(ctrl_space, (130, 320))
        screen.blit(ctrl_ready, (130, 340))
        screen.blit(ctrl_reset, (130, 360))
        screen.blit(ctrl_screen, (130, 380))

        pygame.draw.rect(screen, BLUE, github_button, border_radius=8)
        gh_text = SMALL_FONT.render("View GitHub Profile", True, WHITE)
        screen.blit(gh_text, gh_text.get_rect(center=github_button.center))

        pygame.draw.rect(screen, BLUE, linkedin_button, border_radius=8)
        li_text = SMALL_FONT.render("Connect on LinkedIn", True, WHITE)
        screen.blit(li_text, li_text.get_rect(center=linkedin_button.center))

    if state==MENU:
        # Background
        headline_menu()
        menubuttons()


    pygame.display.flip()
    clock.tick(60)
pygame.quit()