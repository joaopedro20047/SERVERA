import pygame

def draw_button(screen, text, x, y, w, h, font, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, w, h)
    hover = button_rect.collidepoint(mouse)

    color = (0, 200, 255) if hover else (0, 150, 255)
    pygame.draw.rect(screen, color, button_rect, border_radius=12)

    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))

    if hover and click[0] == 1 and action:
        action()

def show_popup(screen, title, message):
    popup_w, popup_h = 500, 200
    popup_x = (screen.get_width() - popup_w) // 2
    popup_y = (screen.get_height() - popup_h) // 2
    popup_rect = pygame.Rect(popup_x, popup_y, popup_w, popup_h)

    font_title = pygame.font.SysFont("arial", 32, bold=True)
    font_msg = pygame.font.SysFont("arial", 22)
    font_btn = pygame.font.SysFont("arial", 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                ok_btn = pygame.Rect(popup_x + popup_w - 110, popup_y + popup_h - 50, 100, 35)
                if ok_btn.collidepoint(mouse):
                    running = False

        pygame.draw.rect(screen, (30, 30, 30), popup_rect, border_radius=12)
        pygame.draw.rect(screen, (255, 0, 0), popup_rect, 2, border_radius=12)

        title_surface = font_title.render(title, True, (255, 0, 0))
        message_surface = font_msg.render(message, True, (255, 255, 255))
        screen.blit(title_surface, (popup_x + 20, popup_y + 20))
        screen.blit(message_surface, (popup_x + 20, popup_y + 70))

        ok_btn = pygame.Rect(popup_x + popup_w - 110, popup_y + popup_h - 50, 100, 35)
        pygame.draw.rect(screen, (0, 200, 255), ok_btn, border_radius=8)
        ok_label = font_btn.render("OK", True, (255, 255, 255))
        screen.blit(ok_label, (ok_btn.x + (ok_btn.width - ok_label.get_width()) // 2, ok_btn.y + 5))

        pygame.display.update()

def main_menu(screen):
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, screen.get_size())

    font = pygame.font.SysFont("arial", 36)
    btn_width, btn_height = 250, 60
    x = 100
    start_y = 150
    spacing = 90

    buttons = ["JOGAR", "LOJA", "BARALHOS", "PERFIL", "CONFIGURAÇÕES"]

    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for i, btn_text in enumerate(buttons):
            draw_button(screen, btn_text, x, start_y + i * spacing, btn_width, btn_height, font,
                        lambda: show_popup(screen, "Jogo em Manutenção", "Por favor aguarde o próximo patch de atualização."))

        title_font = pygame.font.SysFont("arial", 72, bold=True)
        title = title_font.render("SERVERA", True, (255, 255, 255))
        screen.blit(title, (screen.get_width() - title.get_width() - 100, screen.get_height() - title.get_height() - 50))

        pygame.display.update()