import sys
import time
import pygame

pygame.init()

# Definindo algumas constantes relativas à aparencia da grade.
PRETO = (0, 0, 0)
CINZA = (128, 128)
AZUL = (66, 133, 250)
LARGURA, ALTURA = 600, 600
TAMANHO_CELULA = 15
LARGURA_GRADE = LARGURA / TAMANHO_CELULA
ALTURA_GRADE = ALTURA / TAMANHO_CELULA
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))

tempo = pygame.time.Clock()

# Desenhando a grade


def desenhando_grade(posicoes):
    for linha in range(ALTURA_GRADE):
        pygame.draw.line(tela, PRETO(0, linha * TAMANHO_CELULA), (LARGURA, linha * TAMANHO_CELULA))


def main():
    rodando = True
    clock = pygame.time.Clock()
    posicoes = set()
    #screen = pygame.Surface(15, 15)

    while rodando:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
                
    #screen.fill(CINZA)                
    desenhando_grade(posicoes)       
    pygame.quit()


if __name__ == '__main__':
    main()
