import pygame
import sys
import time

# Inicialização
pygame.init()
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Servera")

# Fonte
font = pygame.font.SysFont("arial", 40)
title_font = pygame.font.SysFont("arial", 80, bold=True)

# Cores
WHITE = (255, 255, 255)
PROGRESS_COLOR = (0, 120, 255)
BG_COLOR = (10, 10, 30)
BUTTON_COLOR = (30, 30, 100)
BUTTON_HOVER = (50, 50, 150)

# Carrega imagem de fundo
background = pygame.image.load("SERVERA.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Função da barra de progresso
def draw_progress_bar(progress):
    bar_width = 800
    bar_height = 30
    bar_x = (screen_width - bar_width) // 2
    bar_y = screen_height - 150
    pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 3)
    inner_width = int(bar_width * progress)
    pygame.draw.rect(screen, PROGRESS_COLOR, (bar_x + 3, bar_y + 3, inner_width - 6, bar_height - 6))

# Tela de carregamento
def show_loading_screen():
    clock = pygame.time.Clock()
    progress = 0
    while progress < 1.0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))
        draw_progress_bar(progress)
        pygame.display.update()
        progress += 0.01
        time.sleep(0.03)
        clock.tick(60)

# Função para criar botão
def draw_button(text, x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Hover
    color = BUTTON_HOVER if x < mouse[0] < x + w and y < mouse[1] < y + h else BUTTON_COLOR

    pygame.draw.rect(screen, color, (x, y, w, h), border_radius=12)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surf, text_rect)

    if click[0] and x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.time.delay(200)
        if action:
            action()

# Janela de manutenção
def show_popup(message):
    popup = pygame.Surface((600, 300))
    popup.fill((20, 20, 60))
    pygame.draw.rect(popup, WHITE, popup.get_rect(), 4, border_radius=15)

    message_text = font.render(message, True, WHITE)
    msg_rect = message_text.get_rect(center=(300, 120))
    popup.blit(message_text, msg_rect)

    ok_text = font.render("OK", True, WHITE)
    ok_rect = pygame.Rect(250, 200, 100, 50)
    pygame.draw.rect(popup, BUTTON_COLOR, ok_rect, border_radius=10)
    popup.blit(ok_text, ok_text.get_rect(center=ok_rect.center))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ok_rect.collidepoint(pygame.mouse.get_pos()[0] - 660, pygame.mouse.get_pos()[1] - 390):
                    return

        screen.blit(popup, (660, 390))
        pygame.display.update()

# Funções dos botões
def jogar():
    show_popup("Jogo em manutenção. Aguarde o próximo patch.")

def em_manutencao():
    show_popup("Função em manutenção.")

# Tela de menu principal
def menu_principal():
    while True:
        screen.fill(BG_COLOR)

        title = title_font.render("SERVERA", True, WHITE)
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))

        draw_button("JOGAR", 800, 300, 300, 70, jogar)
        draw_button("LOJA", 800, 400, 300, 70, em_manutencao)
        draw_button("BARALHOS", 800, 500, 300, 70, em_manutencao)
        draw_button("PERFIL", 800, 600, 300, 70, em_manutencao)
        draw_button("CONFIGURAÇÕES", 800, 700, 300, 70, em_manutencao)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Executa a tela de loading e o menu principal
show_loading_screen()
menu_principal()
