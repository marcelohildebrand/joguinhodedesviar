import pygame
import random
import math
import os
import json
from datetime import datetime

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desvie das Formas")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)

# Classe do jogador (círculo)
class Player:
    def __init__(self):
        self.radius = 20
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        
        # Mantém o jogador dentro da tela
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.radius)

# Classe das formas inimigas
class Enemy:
    def __init__(self):
        self.shape = random.choice(['square', 'triangle'])
        self.size = random.randint(20, 40)
        self.x = random.randint(0, WIDTH)
        self.y = -self.size
        self.speed = random.uniform(2, 5)
        self.angle = random.uniform(-0.5, 0.5)

    def move(self):
        self.y += self.speed
        self.x += self.angle

    def draw(self):
        if self.shape == 'square':
            pygame.draw.rect(screen, RED, (self.x - self.size/2, self.y - self.size/2, self.size, self.size))
        elif self.shape == 'triangle':
            points = [
                (self.x, self.y - self.size/2),
                (self.x - self.size/2, self.y + self.size/2),
                (self.x + self.size/2, self.y + self.size/2)
            ]
            pygame.draw.polygon(screen, RED, points)

    def collide(self, player):
        # Verificação de colisão simplificada
        dist = math.sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        return dist < (player.radius + self.size/2)

# Funções para gerenciar histórico e leaderboard
def carregar_historico():
    if os.path.exists('historico.json'):
        try:
            with open('historico.json', 'r') as f:
                return json.load(f)
        except:
            return {'partidas': [], 'leaderboard': []}
    else:
        return {'partidas': [], 'leaderboard': []}

def salvar_historico(historico):
    with open('historico.json', 'w') as f:
        json.dump(historico, f)

def atualizar_historico(score):
    historico = carregar_historico()
    
    # Adicionar nova partida ao histórico
    partida = {
        'data': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'pontuacao': score
    }
    historico['partidas'].append(partida)
    
    # Atualizar leaderboard
    historico['leaderboard'].append({'pontuacao': score, 'data': partida['data']})
    historico['leaderboard'] = sorted(historico['leaderboard'], key=lambda x: x['pontuacao'], reverse=True)[:10]
    
    salvar_historico(historico)
    return historico['leaderboard']

# Variáveis do jogo
player = Player()
enemies = []
spawn_rate = 60  # Frames entre cada spawn
spawn_timer = 0
lives = 3
score = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Estados do jogo
running = True
game_over = False
showing_leaderboard = False

# Carrega o histórico e o leaderboard inicial
historico = carregar_historico()
leaderboard = historico.get('leaderboard', [])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:  # Reiniciar jogo
                    lives = 3
                    score = 0
                    enemies.clear()
                    player.x = WIDTH // 2
                    player.y = HEIGHT // 2
                    game_over = False
                    showing_leaderboard = False
                elif event.key == pygame.K_l:  # Mostrar/esconder leaderboard
                    showing_leaderboard = not showing_leaderboard

    if not game_over:
        # Controles
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Spawn de inimigos
        spawn_timer += 1
        if spawn_timer >= spawn_rate:
            enemies.append(Enemy())
            spawn_timer = 0

        # Atualização dos inimigos
        for enemy in enemies[:]:
            enemy.move()
            if enemy.y > HEIGHT + enemy.size:
                enemies.remove(enemy)
                score += 10

            # Verificação de colisão
            if enemy.collide(player):
                enemies.remove(enemy)
                lives -= 1
                if lives <= 0:
                    game_over = True
                    leaderboard = atualizar_historico(score)

        # Atualização da pontuação
        score += 1

    # Desenho
    screen.fill(BLACK)
    
    if not game_over:
        player.draw()
        for enemy in enemies:
            enemy.draw()

        # Interface
        lives_text = font.render(f"Vidas: {lives}", True, WHITE)
        score_text = font.render(f"Pontuação: {score}", True, WHITE)
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (10, 40))
    else:
        game_over_text = font.render(f"Game Over! Pontuação: {score}", True, WHITE)
        restart_text = font.render("Pressione R para reiniciar", True, WHITE)
        leaderboard_text = font.render("Pressione L para ver o leaderboard", True, WHITE)
        
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2 - 60))
        screen.blit(restart_text, (WIDTH//2 - 150, HEIGHT//2))
        screen.blit(leaderboard_text, (WIDTH//2 - 150, HEIGHT//2 + 40))
        
        if showing_leaderboard:
            # Desenhar fundo do leaderboard
            pygame.draw.rect(screen, (50, 50, 50), (WIDTH//2 - 200, HEIGHT//2 - 200, 400, 350))
            pygame.draw.rect(screen, WHITE, (WIDTH//2 - 200, HEIGHT//2 - 200, 400, 350), 2)
            
            # Título do leaderboard
            title_text = font.render("TOP 10 PONTUAÇÕES", True, WHITE)
            screen.blit(title_text, (WIDTH//2 - 120, HEIGHT//2 - 180))
            
            # Mostrar as pontuações
            y_pos = HEIGHT//2 - 130
            for i, entry in enumerate(leaderboard):
                color = WHITE
                if i == 0:
                    color = GOLD
                elif i == 1:
                    color = SILVER
                elif i == 2:
                    color = BRONZE
                
                entry_text = small_font.render(f"{i+1}. {entry['pontuacao']} pts - {entry['data']}", True, color)
                screen.blit(entry_text, (WIDTH//2 - 180, y_pos))
                y_pos += 30

    pygame.display.flip()
    clock.tick(60)

pygame.quit()