import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Café com Açúcar')

# Definir cores
WHITE = (255, 255, 255)  # Cor branca para o cubo de açúcar
BROWN = (139, 69, 19)  # Cor para a xícara
BLACK = (0, 0, 0)  # Cor para o contorno

# Carregar recursos
background_image = pygame.image.load('background.jpeg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Redimensionar imagem de fundo
pygame.mixer.music.load('v.1 (2_13).mp3')
pygame.mixer.music.play(-1)  # Toca a música em loop

# Configurar o objeto (xícara)
cup_width = 100
cup_height = 50
cup_rect = pygame.Rect(SCREEN_WIDTH // 2 - cup_width // 2, SCREEN_HEIGHT - 60, cup_width, cup_height)
cup_speed = 10  # Aumentar a velocidade da xícara
cup_outline_width = 3  # Largura do contorno da xícara

# Configurar os cubos de açúcar
num_sugar_cubes = 5  # Número de cubos de açúcar
sugar_width = 30
sugar_height = 30
sugar_speed = 5
sugar_outline_width = 3  # Largura do contorno dos cubos de açúcar

# Criar uma lista para armazenar os cubos de açúcar
sugar_cubes = []
for _ in range(num_sugar_cubes):
    sugar_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - sugar_width),
                             random.randint(-SCREEN_HEIGHT, -sugar_height),
                             sugar_width,
                             sugar_height)
    sugar_cubes.append(sugar_rect)

# Configurar o relógio
clock = pygame.time.Clock()

# Função para verificar colisão
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Função para desenhar retângulos com contorno
def draw_rect_with_outline(surface, color, rect, outline_color, outline_width):
    pygame.draw.rect(surface, outline_color, rect, outline_width)
    pygame.draw.rect(surface, color, rect)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controlar a movimentação da xícara
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cup_rect.x -= cup_speed
    if keys[pygame.K_RIGHT]:
        cup_rect.x += cup_speed

    # Atualizar a posição dos cubos de açúcar
    for sugar_rect in sugar_cubes:
        sugar_rect.y += sugar_speed
        # Reposicionar cubos que saíram da tela
        if sugar_rect.y > SCREEN_HEIGHT:
            sugar_rect.x = random.randint(0, SCREEN_WIDTH - sugar_width)
            sugar_rect.y = random.randint(-SCREEN_HEIGHT, -sugar_height)

    # Verificar colisão
    for sugar_rect in sugar_cubes:
        if check_collision(cup_rect, sugar_rect):
            sugar_rect.x = random.randint(0, SCREEN_WIDTH - sugar_width)
            sugar_rect.y = random.randint(-SCREEN_HEIGHT, -sugar_height)

    # Desenhar o plano de fundo e os objetos
    screen.blit(background_image, (0, 0))  # Desenhar plano de fundo
    draw_rect_with_outline(screen, BROWN, cup_rect, BLACK, cup_outline_width)  # xícara com contorno
    for sugar_rect in sugar_cubes:
        draw_rect_with_outline(screen, WHITE, sugar_rect, BLACK, sugar_outline_width)  # cubo de açúcar com contorno

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    clock.tick(30)

pygame.quit()
