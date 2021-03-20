import pygame


class Alien:
    """Класс для управления alien."""

    def __init__(self, ai_game):
        """Инициализирует alien и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/monster-2776854_1280.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.center = self.screen_rect = (100, 150)

    def blitme(self):
        """Рисует alien в текущей позиции."""
        self.screen.blit(self.image, self.rect)
