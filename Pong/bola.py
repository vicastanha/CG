# bola.py

import pygame
import random

BRANCO = (255, 255, 255)

class Bola:
    def __init__(self, x, y, tamanho, velocidade_x, velocidade_y):
        self.rect = pygame.Rect(x, y, tamanho, tamanho)
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.cor = BRANCO

    def move(self):
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Colisão com as bordas superiores e inferiores
        if self.rect.y <= 0 or self.rect.y >= pygame.display.get_surface().get_height() - self.rect.width:
            self.velocidade_y = -self.velocidade_y
            self.mudar_cor_e_direcao()

    def colidir(self, raquete):
        if self.rect.colliderect(raquete.rect):
            self.velocidade_x = -self.velocidade_x
            deslocamento = (self.rect.y + self.rect.height / 2) - (raquete.rect.y + raquete.rect.height / 2)
            self.velocidade_y += deslocamento // 20

    def reset_posicao(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.cor, self.rect)

    def mudar_cor_e_direcao(self):
        self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocidade_x += random.choice([-1, 1])
        self.velocidade_y += random.choice([-1, 1])
