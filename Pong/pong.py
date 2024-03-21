import pygame
import sys

pygame.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

#Definição da raquete
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 10

#Posição da Raquete do Lado Esquerdo (PC)
pc_x = 10 #
pc_y = altura // 2  - raquete_altura // 2; 

#Posição da Raquete do Lado Direito (Player 01)
player_1_x = largura - 20
player_1_y = altura // 2  - raquete_altura // 2

#Posição da Bola
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

#Define a velocidade das raquetes
raquete_player_1_dy = 5
raquete_pc_dy = 5

#definindo um limite de velocidade 
clock = pygame.time.Clock()
    

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #preenche o atributo 'Screen' com a cor 'PRETO'            
    screen.fill(PRETO)

     #Desenha a raquete do lado esquerdo
    pygame.draw.rect(screen,BRANCO,(pc_x, pc_y, raquete_largura, raquete_altura))
    
    #Desenha a raquete do lado esquerdo
    pygame.draw.rect(screen,BRANCO,(player_1_x, player_1_y, raquete_largura, raquete_altura))

    #desenhar a bola
    pygame.draw.ellipse(screen, BRANCO,(bola_x, bola_y, tamanho_bola, tamanho_bola))    
    
    #É um atributo q cria uma variavel que vai pega o teclado e chamar a função get_pressed
    keys = pygame.key.get_pressed()
    
    #se a tecla selecionada for o up  e a altura da raquete for maior que zero, ele deverá fazer
    
    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy #menos vai pra cima pq o limite é zero 
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura: # 
        player_1_y += raquete_player_1_dy
    
    clock.tick(120)
    
    pygame.display.flip()

pygame.quit()
sys.exit() #liberar a memoria no sistema e não sobrecarrega