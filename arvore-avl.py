# fator de balanceamento = altura do filho esq - altura filho dir
# nó vazio tem por definição altura = -1
# fator de balanceamento de qlqr nó é -1, 0, 1

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
    elif dado <raiz.dado: #inserir na esq
        raiz.esq = insere(raiz.esq, dado)
        if fatorBalanceamento(raiz) == 2:
            if dado > raiz.esq.dado: #adicionei no meio
                raiz.esq = rotacionaEsquerda(raiz.esq)
            raiz = rotacionaDireita(raiz)
    elif dado > raiz.dado: #inserir na dir
        raiz.dir = insere(raiz.dir, dado)

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


if __name__  == "__main__":
    
    arvore = None
    arvore = insere(arvore, 6)
    arvore = insere(arvore, 4)
    imprime(arvore)
    print()

    arvore = insere(arvore, 5)
    imprime(arvore)
    print()
