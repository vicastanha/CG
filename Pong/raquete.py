import pygame

BRANCO = (255, 255, 255)

class Raquete:
    def __init__(self, x, y, largura, altura, dy):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.dy = dy

    def move_player(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.y > 0:
            self.rect.y -= self.dy
        if keys[down] and self.rect.y < pygame.display.get_surface().get_height() - self.rect.height:
            self.rect.y += self.dy

    def move_ai(self, bola_y):
        if self.rect.y + self.rect.height // 2 < bola_y:
            self.rect.y += self.dy
        elif self.rect.y + self.rect.height // 2 > bola_y:
            self.rect.y -= self.dy
        self.rect.y = max(0, min(self.rect.y, pygame.display.get_surface().get_height() - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, BRANCO, self.rect)