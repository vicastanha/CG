import sys 
import pygame

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0,0,0)
BRANCO = (255,255,255)

tamanho_fonte = 50
fonte = pygame.font.SysFont (None, tamanho_fonte)

texto = fonte.render("Vitoria", True, BRANCO)
# texto_rect = texto.get_rect(center=(largura-60,altura/2)) #MEIO-DIREITA
# texto_rect = texto.get_rect(center=(largura/2, altura/2)) #CENTRO
# texto_rect = texto.get_rect(center=(largura-740,altura/2)) #MEIO-ESQUERDA
#---------------------------------------------------------------------------
# texto_rect = texto.get_rect(center=(largura-740,altura-575)) #Topo-esquerda
# texto_rect = texto.get_rect(center=(largura/2,altura-575)) #TOPO
# texto_rect = texto.get_rect(center=(largura-60,altura-575)) #TOPO-DIREITA
#---------------------------------------------------------------------------
# texto_rect = texto.get_rect(center=(largura/2,altura-25)) #EMBAIXO
#texto_rect = texto.get_rect(center=(largura-60,altura-25)) #EMBAIXO-DIREITA
#texto_rect = texto.get_rect(center=(largura-740, altura-25)) #EMBAIXO-ESQUERDA

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()

