import pygame

class Background:
    def __init__(self):
        self.image = pygame.image.load("assets\\Game Objects\\background-day.png").convert()
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