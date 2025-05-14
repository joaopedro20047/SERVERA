import pygame
import sys
from loading import loading_screen
from main_menu import main_menu

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Servera")
clock = pygame.time.Clock()

loading_screen(screen)
main_menu(screen)