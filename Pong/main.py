# main.py

import pygame
import sys
from jogo import Jogo

LARGURA = 800
ALTURA = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    jogo = Jogo(LARGURA, ALTURA)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        jogo.atualizar(screen)
        pygame.display.flip()
        clock.tick(60)

        if jogo.score_pc == 5 or jogo.score_player == 5:
            jogo.fim_jogo(screen)

if __name__ == "__main__":
    main()
