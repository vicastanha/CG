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

#Define a velocidade da bola
velocidade_bola_x = 3
velocidade_bola_y = 3

#Define o score
score_player_1 = 0
score_pc = 0

# Configuração da fonte
font_file = "font/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_file, 24)

#definindo um limite de velocidade 
clock = pygame.time.Clock()

rodando = False

def menu_principal():
    global rodando
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rodando = True
                    return
                
        #Renderiza o texto do menu
        screen.fill(PRETO)
        texto_menu = font.render("Pong", True, BRANCO)
        texto_menu_rect = texto_menu.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_menu, texto_menu_rect)
       
        
        tempo = pygame.time.get_ticks()
        #Pressione SPACE para iniciar o jogo
        if tempo % 2000 < 1000:
             texto_iniciar = font.render("> Press SPACE to Start <", True, BRANCO)
             texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
             screen.blit(texto_iniciar, texto_iniciar_rect)
             
        pygame.display.flip()

def posicao_inicial():
    pass

def fim_jogo():
    global rodando
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Renderizar o texto do menu
        screen.fill(PRETO)
        texto_fim = font.render("Fim do Jogo :/", True, BRANCO)
        text_fim_rect = texto_fim.get_rect(center=(largura // 2, altura // 2 ))
        screen.blit(texto_fim, text_fim_rect)
        
        pygame.display.flip() 


menu_principal()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #preenche o atributo 'Screen' com a cor 'PRETO'            
    screen.fill(PRETO)

    #Movendo Bola
    bola_x+= velocidade_bola_x
    bola_y+= velocidade_bola_y
    
    #Retângulos de Colisão
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola)
    raquete_pc_rect = pygame.Rect(pc_x,pc_y, raquete_largura,raquete_altura)
    raquete_player_1_rect = pygame.Rect(
        player_1_x, player_1_y, raquete_largura, raquete_altura
    )

    #Colisão da bola com a raquete do pc e a raquete do player
    if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(raquete_player_1_rect):
        velocidade_bola_x = -velocidade_bola_x
        
    #Colisão da bola com o limite da tela
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        velocidade_bola_y = -velocidade_bola_y

    # Posicionar a bola no início do jogo
    if bola_x <= 0:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = largura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x
        score_player_1 += 1
        print(f"Score Player 1: {score_player_1}")
        if score_player_1 == 5:
            print("Player_1 ganhou!")
            rodando = False
    
    if bola_x >= largura - tamanho_bola:
        bola_x = largura // 2 - tamanho_bola // 2
        bola_y = largura // 2 - tamanho_bola // 2
        velocidade_bola_x = -velocidade_bola_x 
        score_pc += 1
        print(f"Score Pc: {score_pc}")
        if score_pc == 5:
            print("O PC ganhou!")
            rodando = False
            
        
    # Movendo a raquete do pc pra seguir a bola
    if pc_y +raquete_altura // 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y +raquete_altura // 2 > bola_y:
        pc_y -= raquete_pc_dy
        
    # Evitar que a raquete do pc saia 
    # da área
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - raquete_altura:
        pc_y = altura - raquete_altura
        
    #Mostrando Score no jogo
    fonte_score = pygame.font.Font(font_file, 24)
    score_texto = fonte_score.render(
        f"Score Player 1: {score_player_1} Score PC: {score_pc}", True, BRANCO
        )
    
    screen_rect = score_texto.get_rect(center = (largura // 2, 50))
    
    screen.blit(score_texto, screen_rect)

     #Desenha a raquete do lado esquerdo
    pygame.draw.rect(screen,BRANCO,(pc_x, pc_y, raquete_largura, raquete_altura))
    #Desenha a raquete do lado esquerdo
    pygame.draw.rect(screen,BRANCO,(player_1_x, player_1_y, raquete_largura, raquete_altura))

    #Desenhar a bola
    pygame.draw.ellipse(screen, BRANCO,(bola_x, bola_y, tamanho_bola, tamanho_bola)) 
    #Desenha uma linha na vertical do meio
    pygame.draw.aaline(screen, BRANCO, (largura // 2, 0), (largura // 2, altura))   
    
    #É um atributo q cria uma variavel que vai pega o teclado e chamar a função get_pressed
    keys = pygame.key.get_pressed()
    
    #se a tecla selecionada for o up  e a altura da raquete for maior que zero, ele deverá fazer

    if keys[pygame.K_UP] and player_1_y > 0:
        player_1_y -= raquete_player_1_dy #menos vai pra cima pq o limite é zero 
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura: # 
        player_1_y += raquete_player_1_dy
    
    pygame.display.flip()
    
    clock.tick(120)
 
fim_jogo()   
# pygame.quit()
# sys.exit() #liberar a memoria no sistema e não sobrecarrega