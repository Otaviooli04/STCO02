# Esta estrutura de dados possui as seguintes propriedades:
#   1. A raiz é preta
#   2. Não há dois nós vermelhos seguidos / Não há links vermelhos seguidos / Não há nós vermelhos com filhos vermelhos
#   3. Todo caminho da raiz até uma folha tem o mesmo número de nós pretos (folha = nó negro None)
#   4. Os nós externos são pretos
#   5. A árvore é perfeitamente balanceada (2-3 tree)
#   6. Sua complexidade de tempo para inserção, busca e remoção é O(logN)
#   7. A altura da árvore é no máximo 2logN
#   8. Todo nó é vermelho ou negro
#   9. (Nesta implementação): Um nó vermelho é filho esquerdo do seu pai
#   10. Altura negra é quantidade de nós pretos que eu passo até chegar a raiz 
#   11. No pior caso, a árvore percorre 2N nós negros para chegar a sua folha

# Resumo do algoritmo de inserção: Se filho direito é rubro e filho esquerdo negro, rode para a esquerda.  
# A: Se filho esquerdo e neto esquerdo-esquerdo são rubros, rode para a direita.  
# B: Se dois filhos são rubros, faça inversão de cores.
# A -> B

# Problema da Binary Search Tree: 
#   você não controla a ordem de entradas dos elementos,
#   podendo resultar num acúmulo de elemento de um lado da Binaty Tree, gerando assim uma árvore desbalanceada

class RedBlackTree:
    RED = True
    BLACK = False
    
    class Node:
        def __init__(self, key, val, N, color): # N é o número de nós na subárvore
            self.key = key # chave de busca
            self.val = val # valor associado à chave
            self.left = None # subárvore esquerda
            self.right = None # subárvore direita
            self.N = N # número de nós na subárvore
            self.color = color # cor do link que conecta o nó ao pai

    def isRed(self, x): # verifica se o nó é vermelho
        if x is None: 
            return False
        return x.color == self.RED
    
    def rotateLeft(self, h): # rotação para a esquerda
        x = h.right # x é o filho direito de h
        h.right = x.left # o filho esquerdo de x se torna o filho direito de h
        x.left = h # h se torna o filho esquerdo de x
        x.color = h.color # a cor de x se torna a cor de h
        h.color = self.RED # a cor de h se torna vermelha
        x.N = h.N # o número de nós de x se torna o número de nós de h
        h.N = 1 + self.size(h.left) + self.size(h.right) # o número de nós de h se torna 1 + o número de nós da subárvore esquerda + o número de nós da subárvore direita
        return x # retorna o nó x
    
    def rotateRight(self, h): # rotação para a direita
        x = h.left # x é o filho esquerdo de h
        h.left = x.right # o filho direito de x se torna o filho esquerdo de h
        x.right = h # h se torna o filho direito de x
        x.color = h.color # a cor de x se torna a cor de h
        h.color = self.RED # a cor de h se torna vermelha
        x.N = h.N # o número de nós de x se torna o número de nós de h
        h.N = 1 + self.size(h.left) + self.size(h.right) # o número de nós de h se torna 1 + o número de nós da subárvore esquerda + o número de nós da subárvore direita
        return x # retorna o nó x
    
    def flipColors(self, h): # troca as cores de h e de seus filhos
        h.color = self.RED # a cor de h se torna vermelha
        h.left.color = self.BLACK # a cor do filho esquerdo de h se torna preta
        h.right.color = self.BLACK # a cor do filho direito de h se torna preta

    def size(self, x): # retorna o número de nós na subárvore
        if x is None: 
            return 0
        return x.N # retorna o número de nós na subárvore

    def __init__(self): # construtor
        self.root = None # raiz da árvore
        self.RED = True # cor vermelha
        self.BLACK = False # cor preta

    def put(self, key, val): # insere um nó na árvore
        self.root = self._put(self.root, key, val) # chama o método privado _put
        self.root.color = self.BLACK # a raiz sempre é preta

    def _put(self, h, key, val): # método privado para inserir um nó na árvore
        if h is None: # se h for None, retorna um novo nó
            return self.Node(key, val, 1, self.RED) # retorna um novo nó com a chave, o valor, o número de nós e a cor passados como parâmetro

        cmp = key.compareTo(h.key) # compara a chave passada como parâmetro com a chave do nó h
        if cmp < 0: # se a chave passada como parâmetro for menor que a chave do nó h, chama o método _put para a subárvore esquerda
            h.left = self._put(h.left, key, val) 
        elif cmp > 0: # se a chave passada como parâmetro for maior que a chave do nó h, chama o método _put para a subárvore direita
            h.right = self._put(h.right, key, val) 
        else: # se a chave passada como parâmetro for igual à chave do nó h, atualiza o valor do nó h
            h.val = val

        if self.isRed(h.right) and not self.isRed(h.left): # se o filho direito de h for vermelho e o filho esquerdo de h não for vermelho, rotaciona h para a esquerda
            h = self.rotateLeft(h) 
        if self.isRed(h.left) and self.isRed(h.left.left): # se o filho esquerdo de h for vermelho e o filho esquerdo do filho esquerdo de h for vermelho, rotaciona h para a direita
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right): # se o filho esquerdo de h e o filho direito de h forem vermelhos, troca as cores de h e de seus filhos
            self.flipColors(h)
        h.N = self.size(h.left) + self.size(h.right) + 1 # atualiza o número de nós de h
        return h # retorna o nó h
    
    

