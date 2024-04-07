import pygame
import random

def respawn_poverh():
    poverh_rect.x = random.randint(0, W - poverh_rect.w)
    poverh_rect.y = random.randint(0, H - poverh_rect.h)
    

pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.font.init()

W = 500
H = 800
SCREEN_SIZE = (W, H)
SCREEN_CENTER = (W // 2, H // 2)
SCREEN_TOP = (W // 2, 0)

screen = pygame.display.set_mode(SCREEN_SIZE)

FPS = 60
clock = pygame.time.Clock()
FONT_PATH = "Mario and Luigi.ttf"
font_large = pygame.font.Font(FONT_PATH, 48)
font_small = pygame.font.Font(FONT_PATH, 24)

TIME_OBJEKT = 2000
finish_delay = TIME_OBJEKT
DECREASE_BASE = 1.002
last_respawn_time = 0

game_over = False
RETRY_SURFACE = font_small.render("PreSS AnY Key" , True, (255, 255, 255))
RETRY_RECT = RETRY_SURFACE.get_rect()
RETRY_RECT.midtop = SCREEN_CENTER

score = 0

POVERH_IMAGE = pygame.image.load("Кнопка.png")
POVERH_IMAGE = pygame.transform.scale(POVERH_IMAGE, (120, 120))
poverh_rect = POVERH_IMAGE.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                score = 0
                finish_delay = TIME_OBJEKT
                game_over = False
                last_respawn_time = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if not game_over and poverh_rect.collidepoint(event.pos) :
                    score += 1
                    respawn_poverh()
                    last_respawn_time = pygame.time.get_ticks()
                    finish_delay = TIME_OBJEKT / (DECREASE_BASE ** score)
    clock.tick(FPS)
    screen.fill((0, 0, 255))
    score_surface = font_large.render(str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect()

    now = pygame.time.get_ticks()
    elapsed = now - last_respawn_time
    if elapsed > finish_delay:
        game_over = True
        score_rect.midbottom = SCREEN_CENTER
        
        screen.blit(RETRY_SURFACE, RETRY_RECT)

    else:
        h = H - H * elapsed / finish_delay
        time_rect = pygame.Rect((0, 0), (W, h))
        time_rect.bottomleft = (0, H)
        pygame.draw.rect(screen, (255, 255, 255,), time_rect)
        screen.blit(POVERH_IMAGE, poverh_rect)

        score_rect.midtop = SCREEN_TOP 

    screen.blit(score_surface, score_rect)

    pygame.display.flip()
pygame.quit
    

  


    
