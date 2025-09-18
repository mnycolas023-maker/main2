import pygame
import os

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) # Janela redimensionável

pygame.display.set_caption("Mover Imagem com Setas")

# Cores
BLACK = (0, 0, 0) # Cor de fundo (no início)

# Carregar a imagem
image_file = "walker-down-3.png" # Coloque o nome do seu imagem aqui!
image = pygame.image.load(os.path.join("assets", image_file)) # Carrega a imagem
image = pygame.transform.scale(image, (64, 64)) # Redimensiona

# Posição inicial da imagem
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2)) # Centraliza a imagem

# Velocidade de movimento
speed = 5 # pode ser ajustado

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Fecha a janela
            running = False

    # Verifica teclas pressionadas continuamente (como o teclado da tela do celular)
    keys = pygame.key.get_pressed()
    
    # Verifica o tamanho da janela (redimensionamento)
    screen_width, screen_height = screen.get_size()

    # Se a imagem foi redimensionada, centraliza
    if screen_width != image_rect.centerx or screen_height != image_rect.centery:
        image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

    # Movimentos com as setas
    if keys[pygame.K_LEFT]:  # Move para a esquerda
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]: # Move para a direita
        image_rect.x += speed
    if keys[pygame.K_UP]:    # Move para cima
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:  # Move para baixo
        image_rect.y += speed

    # Preencher o fundo
    screen.fill(BLACK)

    # Desenhar a imagem na tela
    screen.blit(image, image_rect)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
