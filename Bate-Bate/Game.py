
import pygame
import sys
from MecMovimento import MovendoTexto


class Game:
    def __init__(self):
        pygame.init()
        self.largura = 800 #definindo valores para a variavel largura
        self.altura = 600 #definindo valores para a variavel altura
        self.tela = pygame.display.set_mode((self.largura, self.altura)) #ele cria esse atributo baseando-se na altura e largura informados
        pygame.display.set_caption("Bate-Bate") #coloca o nome na janela
        self.clock = pygame.time.Clock()  #cria um atributo e chama o método clock da biblioteca pygame
        self.MovendoTexto = MovendoTexto("Vitória", 50, self.largura, self.altura) #cria um atributo pra criar o retangulo com o nome respeitando o tamanho (altura x largura) baseado no tamanho da fonte tbm

    def run(self): #método voltado para rodar e abrir a tela com o 'joguinho'
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            self.MovendoTexto.move() #aplica o método move no atributo MovendoTexto
            self.tela.fill((0, 0, 0))
            self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)
            pygame.display.flip() #aplica o método flip 
            self.clock.tick(60) #seta um valor do tick para 60

        pygame.quit()
        sys.exit()
