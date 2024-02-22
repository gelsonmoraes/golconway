import sys
import time
import pygame

pygame.init()

# Definindo algumas constantes relativas à aparencia da grade.
PRETO = (13, 13, 13)
CINZA = (65, 65, 65)
AZUL = (0, 30, 212)
VERMELHO = (255, 5, 5)
LARGURA, ALTURA = 660, 660
TAMANHO_CELULA = 33
LARGURA_GRADE = LARGURA // TAMANHO_CELULA
ALTURA_GRADE = ALTURA // TAMANHO_CELULA
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
tempo = pygame.time.Clock()

# Desenhando a grade
def desenhando_grade(posicoes):

    for posicao in posicoes:
        coluna, linha = posicao
        superior_esquerdo = (coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA)
        pygame.draw.rect(tela, AZUL, (*superior_esquerdo,TAMANHO_CELULA, TAMANHO_CELULA))

    for linha in range(int(ALTURA_GRADE)):
        pygame.draw.line(tela, PRETO, (0, linha * TAMANHO_CELULA),
                         (LARGURA, linha * TAMANHO_CELULA))

    for coluna in range(int(ALTURA_GRADE)):
        pygame.draw.line(tela, PRETO, (coluna * TAMANHO_CELULA,
                         0), (coluna * TAMANHO_CELULA, ALTURA))


def main():
    rodando = True
    posicoes = set()

    while rodando:
        tempo.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                
            #Implementa a funcionalidade de mudar o estado da célula ao clicar na mesma.    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                coluna = x // TAMANHO_CELULA
                linha = y // TAMANHO_CELULA
                pos = (coluna, linha)
                if pos in posicoes:
                    posicoes.remove(pos)
                else:
                    posicoes.add(pos)

        tela.fill(CINZA)
        desenhando_grade(posicoes)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
