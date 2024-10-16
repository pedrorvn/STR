import pygame
import random
import time

# Inicialização do Pygame
pygame.init()

# Cores
COR = {
    'r': (255, 0, 0),
    'g': (0, 255, 0),
    'b': (0, 0, 255),
    'y': (255, 255, 0),
    'white': (255, 255, 255)
}

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo das Bolinhas")

# Variáveis do jogo
num_bolinas = 0
bolinas = []
tempo_reacao = 0
acertos = 0
tempo_inicio = None

def gera_bolinha():
    global num_bolinas, tempo_inicio
    if num_bolinas < 10:  # Limite de 10 bolinhas
        cor = random.choice(list(COR.keys())[:-1])  # Escolhe uma cor aleatória
        # Garante que a bolinha não saia da tela
        x = random.randint(30, LARGURA - 30)  
        y = random.randint(30, ALTURA - 30)  
        bolinas.append((cor, x, y))
        num_bolinas += 1
        tempo_inicio = time.time()  # Reinicia o tempo
        print(f"Bolinha gerada: Cor {cor}, Posição ({x}, {y})")  # Depuração

def desenha_bolinas():
    for bolina in bolinas:
        pygame.draw.circle(tela, COR[bolina[0]], (bolina[1], bolina[2]), 30)

def jogo():
    global tempo_reacao, acertos, num_bolinas
    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Detecta pressionamento de teclas para acertar bolinhas
            if evento.type == pygame.KEYDOWN:
                if evento.unicode in COR.keys() and num_bolinas > 0:
                    cor_atual = bolinas[-1][0]  # Pega a cor da bolinha atual
                    if evento.unicode == cor_atual:  # Verifica se a tecla pressionada corresponde à bolinha
                        tempo_reacao += (time.time() - tempo_inicio) * 1000  # Converte para milissegundos
                        acertos += 1
                        bolinas.pop()  # Remove a bolinha acertada
                        gera_bolinha()  # Gera uma nova bolinha
                        print(f"Bolinha acertada! Total de acertos: {acertos}")  # Depuração

        tela.fill(COR['white'])  # Limpa a tela
        desenha_bolinas()  # Desenha bolinhas

        pygame.display.flip()  # Atualiza a tela
        clock.tick(60)  # Limita a 60 FPS

        if num_bolinas >= 10:  # Termina o jogo após 10 bolinhas
            rodando = False

    pygame.quit()

# Inicia o jogo
gera_bolinha()  # Gera a primeira bolinha
jogo()

# Exibe os resultados finais
if acertos > 0:
    print(f"Tempo médio de reação: {tempo_reacao / acertos:.2f} milissegundos")  # Exibe em milissegundos
else:
    print("Nenhuma bolinha acertada. Não foi possível calcular o tempo médio de reação.")
print(f"Pontuação de acertos: {acertos}")
