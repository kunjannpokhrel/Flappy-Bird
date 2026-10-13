import pygame

class Background:
    def __init__(self,bg_no):
            self.image = pygame.image.load(f"assets\\Background\\background{bg_no}.png").convert()
            self.image = pygame.transform.scale(self.image,(800,600))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

class Ground:
    def __init__(self):
        self.image = pygame.image.load("assets\\Game Objects\\base.png").convert()
        self.image = pygame.transform.scale(self.image,(800,50))

    def draw(self, screen):
        screen.blit(self.image, (0, 550))

class Bird:
    def __init__(self):
        self.image = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-midflap.png").convert()
        self.image = pygame.transform.scale(self.image,(34,24))

    def draw(self, screen):
        screen.blit(self.image, (380, 280))

class Click:
    def __init__(self):
        self.music = pygame.mixer.Sound("assets\\Sound Efects\\click.mp3")
        self.music.set_volume(1)

    def play(self):
        self.music.play()
