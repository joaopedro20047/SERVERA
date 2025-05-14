import pygame
import time

def loading_screen(screen):
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, screen.get_size())

    font = pygame.font.SysFont("arial", 48)
    small_font = pygame.font.SysFont("arial", 24)

    progress_width = 600
    progress_height = 30
    progress_x = (screen.get_width() - progress_width) // 2
    progress_y = screen.get_height() - 100

    for i in range(101):
        screen.blit(background, (0, 0))
        loading_text = font.render("CARREGANDO...", True, (255, 255, 255))
        screen.blit(loading_text, ((screen.get_width() - loading_text.get_width()) // 2, progress_y - 60))
        pygame.draw.rect(screen, (255, 255, 255), (progress_x, progress_y, progress_width, progress_height), 2)
        pygame.draw.rect(screen, (0, 200, 255), (progress_x + 2, progress_y + 2, int((progress_width - 4) * (i / 100)), progress_height - 4))
        pygame.display.update()
        time.sleep(0.01)