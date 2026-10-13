import pygame

class Background:
    def __init__(self,bg_no):
            self.image = pygame.image.load(f"assets\\Background\\background{bg_no}.png").convert()
            self.image = pygame.transform.scale(self.image,(800,600))
            self.x1=0
            self.x2=800
            self.speed=1

    def update(self):
        self.x1-=self.speed
        self.x2-=self.speed

        if self.x2<=0:
            self.x2+=800
        elif self.x1<=-800:
            self.x1+=800

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))

class Ground:
    def __init__(self):
        self.image = pygame.image.load("assets\\Game Objects\\base.png").convert()
        self.image = pygame.transform.scale(self.image,(800,50))
        self.x1=0
        self.x2=800
        self.speed=3

    def update(self):
        self.x1-=self.speed
        self.x2-=self.speed

        if self.x2<=0:
            self.x2+=800
        elif self.x1<=-800:
            self.x1+=800

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 550))
        screen.blit(self.image, (self.x2, 550))

class Bird:
    def __init__(self):
        self.mid_image = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-midflap.png").convert_alpha()
        self.mid_image = pygame.transform.scale(self.mid_image,(34,24))
        self.down_image = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-downflap.png").convert_alpha()
        self.down_image  = pygame.transform.scale(self.down_image,(34,24))
        self.up_image = pygame.image.load("assets\\Game Objects\\yellowbird\\yellowbird-upflap.png").convert_alpha()
        self.up_image = pygame.transform.scale(self.up_image,(34,24))
        self.image=self.mid_image

        self.y=250
        self.gravity=0.3
        self.jump_strength=7
        self.velocity=0  

    def update(self):
        self.velocity+=self.gravity
        self.y+=self.velocity
        self.gravity+=0.001
        if self.y<=0:
            self.y=0
            self.velocity=0
        if self.y>=525:
            self.y=525
            self.velocity=0

        if self.velocity < -2:
            self.image = self.up_image
        elif self.velocity > 2:
            self.image = self.down_image
        else:
            self.image = self.mid_image

    def space(self):
        self.velocity=-self.jump_strength
        self.gravity=0.3



    def draw(self, screen,):
        screen.blit(self.image, (380, self.y))

class Click:
    def __init__(self):
        self.music = pygame.mixer.Sound("assets\\Sound Efects\\click.mp3")
        self.music.set_volume(1)

    def play(self):
        self.music.play()
