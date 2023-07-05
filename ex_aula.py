#Otávio Henrique Rodrigues de Oliveira/ 2022004912
# Wesley Batista Luz / 2023008237

# D (tam do tabuleiro)
# N (num de jogadas)
# N pontos(x,y)

from ponto import ponto
import random

#------------------------------------------------------------------------------------
class noh:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.altura = 0



def imprime(raiz):
    if raiz == None:
        return
    print('[' + str(raiz.dado), end=", ")
    imprime(raiz.esq)
    print(", ", end='')
    imprime(raiz.dir)
    print("]", end='')

def fatorBalanceamento(raiz):
    return altura(raiz.esq) - altura(raiz.dir)

def insere(raiz, dado):
    if raiz == None:
        return noh(dado)
    
    if raiz.dado == dado: #dado repetido não será inserido
        return raiz
    elif dado < raiz.dado: #inserir na esq
        raiz.esq = insere(raiz.esq, dado)
        if fatorBalanceamento(raiz) == 2:
            if dado > raiz.esq.dado: #adicionei no meio
                raiz.esq = rotacionaEsquerda(raiz.esq)
            raiz = rotacionaDireita(raiz)
    elif dado > raiz.dado: #inserir na dir
        raiz.dir = insere(raiz.dir, dado)
        if fatorBalanceamento(raiz) == -2:
            if dado < raiz.dir.dado: #adicionei no meio
                raiz.dir = rotacionaDireita(raiz.dir)
            raiz = rotacionaEsquerda(raiz)

    #arruma altura
    raiz.altura = max(altura(raiz.esq), altura(raiz.dir)) + 1
    return raiz

def altura(raiz):
    if raiz == None:
        return -1
    return raiz.altura

def rotacionaDireita(y):
    novaRaiz = y.esq
    y.esq = novaRaiz.dir
    novaRaiz.dir = y

    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    novaRaiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir))

    return novaRaiz

def rotacionaEsquerda(y):
    novaRaiz = y.dir
    y.dir = novaRaiz.esq
    novaRaiz.esq = y

    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    novaRaiz.altura = max(altura(novaRaiz.esq), altura(novaRaiz.dir))

    return novaRaiz

def busca(raiz, valor):
    if raiz == None:
        return False
    if raiz.dado == valor:
        return True
    elif valor < raiz.dado:
        return busca(raiz.esq, valor)
    elif valor > raiz.dado:
        return busca(raiz.dir, valor)



#-------------------------------------------------------------------------------------

D = int(input())
N = int(input())

arvore_pontos = None

for i in range(N):
    linha = input()
    lista = linha.split()
    x, y =[int(k) for k in lista]
    novo = ponto(x, y)
    arvore_pontos = insere(arvore_pontos, novo)

random.seed(42)

dano = 0

for i in range(N):
    x = random.randint(0, D)
    y = random.randint(0, D)
    # print("foi para " + str(x) + ", " + str(y))

    novo = ponto(x, y)
    if busca(arvore_pontos, novo) == True:
        dano += 1

print("Tomou " + str(dano) + " de dano")


