import pygame
import random


class MovendoTexto:
    def __init__(self, texto, fonte_tamanho, largura, altura):
        self.fonte = pygame.font.SysFont(None, fonte_tamanho) #criar
        self.texto = texto
        self.largura = largura
        self.altura = altura
        self.texto_surf = self.fonte.render(texto, True, (255, 255, 255))
        self.rect = self.texto_surf.get_rect(center=(largura / 2, altura / 2))

        self.velocidade_x = self.gerar_numero_nao_zero()
        self.velocidade_y = self.gerar_numero_nao_zero()

    def gerar_numero_nao_zero(self):
        numero = 0
        while numero == 0: # enquanto a variavel numero é igual a zero 
            numero = random.randint(-1, 1) #
        return numero

    def move(self): # método para setar as velocidades
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.left <= 0: #evita pra bater no máximo da esquerda
            self.velocidade_x = random.randint(0, 1)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.right >= self.largura: #evita pra bater no máximo da direita
            self.velocidade_x = random.randint(-1, 0)
            self.velocidade_y = random.randint(-1, 1)
            self.change_color()

        if self.rect.top <= 0: #evita pra bater em cima
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(0, 1)
            self.change_color()

        if self.rect.bottom >= self.altura:  #evita pra bater  embaixo
            self.velocidade_x = random.randint(-1, 1)
            self.velocidade_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self): #gera uma cor aleatorio e troca ela
        cor_texto = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.texto_surf = self.fonte.render(self.texto, True, cor_texto)