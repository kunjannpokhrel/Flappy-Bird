import pygame
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("FLAPPY BIRD")
clock=pygame.time.Clock()

running=True
while running:
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
            running=False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
