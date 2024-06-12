import pygame
from raquete import Raquete
from bola import Bola

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
FONT_FILE = "Pong/font/PressStart2P-Regular.ttf"

class Jogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.raquete_pc = Raquete(10, altura // 2 - 30, 10, 60, 5)
        self.raquete_player = Raquete(largura - 20, altura // 2 - 30, 10, 60, 5)
        self.bolas = [Bola(largura // 2 - 5, altura // 2 - 5, 10, 3, 3)]
        self.score_pc = 0
        self.score_player = 0
        self.tempo_jogo = pygame.time.get_ticks()
        self.font = pygame.font.Font(FONT_FILE, 36)
        self.font_score = pygame.font.Font(FONT_FILE, 16)

    def resetar_jogo(self):
        self.raquete_pc.rect.y = self.altura // 2 - 30
        self.raquete_player.rect.y = self.altura // 2 - 30
        self.bolas = [Bola(self.largura // 2 - 5, self.altura // 2 - 5, 10, 3, 3)]
        self.score_pc = 0
        self.score_player = 0
        self.tempo_jogo = pygame.time.get_ticks()

    def adicionar_bola(self):
        if len(self.bolas) < 3:  # Limite de 3 bolas
            nova_bola = Bola(self.largura // 2 - 5, self.altura // 2 - 5, 10, 3, 3)
            self.bolas.append(nova_bola)

    def atualizar(self, screen):
        screen.fill(PRETO)

        for bola in self.bolas:
            bola.move()
            bola.colidir(self.raquete_pc)
            bola.colidir(self.raquete_player)

            # Posicionar a bola no início do jogo
            if bola.rect.x <= 0:
                self.score_player += 1
                bola.reset_posicao(self.largura // 2 - 5, self.altura // 2 - 5)
            if bola.rect.x >= self.largura - bola.rect.width:
                self.score_pc += 1
                bola.reset_posicao(self.largura // 2 - 5, self.altura // 2 - 5)

            bola.draw(screen)

        self.raquete_pc.draw(screen)
        self.raquete_player.draw(screen)
        pygame.draw.aaline(screen, BRANCO, (self.largura // 2, 0), (self.largura // 2, self.altura))

        self.raquete_player.move_player(pygame.K_UP, pygame.K_DOWN)
        if self.bolas:
            self.raquete_pc.move_ai(self.bolas[0].rect.y)

        # Mostrar pontuação no jogo
        score_texto = self.font_score.render(f"Score PC: {self.score_pc}   Score Player: {self.score_player}", True, BRANCO)
        score_rect = score_texto.get_rect(center=(self.largura // 2, 30))
        screen.blit(score_texto, score_rect)

        # Adiciona uma nova bola ou aumenta a velocidade após 30 segundos
        if pygame.time.get_ticks() - self.tempo_jogo > 30000:
            self.adicionar_bola()
            for bola in self.bolas:
                bola.velocidade_x += 1
                bola.velocidade_y += 1
            self.tempo_jogo = pygame.time.get_ticks()

    def fim_jogo(self, screen):
        vencedor = "PC" if self.score_pc == 5 else "Player"
        screen.fill(PRETO)
        texto_fim = self.font.render(f"Vencedor: {vencedor}", True, BRANCO)
        text_fim_rect = texto_fim.get_rect(center=(self.largura // 2, self.altura // 2))
        screen.blit(texto_fim, text_fim_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.resetar_jogo()