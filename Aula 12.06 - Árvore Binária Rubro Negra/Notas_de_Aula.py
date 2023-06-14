class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.cor = True
        
def isRed(raiz):
    if raiz is None:
        return False
    else:
        return raiz.cor == True
    
def isBlack(raiz):
    if raiz is None:
        return True
    else:
        raiz.cor == False
        
def sobeVermelho(raiz):
    raiz.cor = True
    raiz.dir.cor = False
    raiz.esq.cor = False
                
def insere_aux(raiz, dado):
    if raiz is None:
         return Noh(dado)
        
    elif dado < raiz.dado:
        raiz.esq = insere_aux(raiz.esq, dado) 
            
    elif dado > raiz.dado:
        raiz.dir = insere_aux(raiz.dir, dado)
            
    else:
        # se o dado já esta na árvore, não faz nada
        return raiz
    
    if isRed(raiz.dir) and isBlack(raiz.esq):
        raiz = rotacionaEsquerda(raiz)
        
    if isRed(raiz.esq) and isRed(raiz.esq.esq):
        raiz = rotacionaDireita(raiz)
        
    if isRed(raiz.esq) and isRed(raiz.dir):
        sobeVermelho(raiz)
        
def insere(raiz, dado):
    raiz = insere_aux(raiz, dado)
    raiz.cor = False
    return raiz

def rotacionaEsquerda(y):
    novaRaiz = y.dir # nova raiz é o filho direito de y
    y.dir = novaRaiz.esq # o filho esquerdo de novaRaiz se torna o filho direito de y
    novaRaiz.esq = y  # y se torna o filho esquerdo de novaRaiz
    novaRaiz.cor = y.cor # a cor de novaRaiz se torna a cor de y
    y.cor = True # a cor de y se torna vermelha
    
def rotacionaDireita(y):
    novaRaiz = y.esq # nova raiz é o filho esquerdo de y
    y.esq = novaRaiz.dir # o filho direito de novaRaiz se torna o filho esquerdo de y
    novaRaiz.dir = y # y se torna o filho direito de novaRaiz
    novaRaiz.cor = y.cor # a cor de novaRaiz se torna a cor de y
    y.cor = True # a cor de y se torna vermelha

def busca(raiz, dado):
    if raiz is None:
        return None
    elif dado < raiz.dado:
        busca(raiz.esq, dado)
    elif dado > raiz.dado:
        busca(raiz.dir, dado)
    else:
        return True

arvore = None
arvore = insere(arvore, 5)
arvore = insere(arvore, 7)
arvore = insere(arvore, 3)
