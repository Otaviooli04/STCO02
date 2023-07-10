# 2022004912 / Otávio Henrique Rodrigues de Oliveira
# 2022010320 / Luis Eduardo Damasceno


#cada nÃ³ tem no minimo t filhos
#cada nÃ³ tem no mÃ¡ximo 2t filhos 

class noh:
    def __init__(self):
        self.folha = True
        self.chaves = []
        self.filhos = []

class arvoreB:
    def __init__(self, t):
        self.t = t
        self.raiz = noh()

    #ESSA EH A FUNCAO QUE VOCÃŠ DEVE FAZER
    #VOCE DEVE CARREGAR DOS ARQUIVOS UMA ARVORE QUE 
    #JA EH VALIDA
    #SUGESTAO: FAZER RECURSIVA
    def le_arquivo(self, nome_arquivo):
        if(nome_arquivo == "None"):
            return None
        f = open(nome_arquivo, "r")
        n = noh()
        
        for linha in f:
            linha = linha.replace("\n", "")
            if ".tree" not in linha and linha != "None":
                linha = int(linha)
                n.chaves.append(linha)
            else:
                n.filhos.append(linha)
            
        for i in range(len(n.filhos)):
            n.filhos[i] = self.le_arquivo(n.filhos[i])

        if all(filho is None for filho in n.filhos):
            n.folha = True
        else:
            n.folha = False

        return n
    
    def carrega_arquivo(self, nome_arquivo):
        self.raiz = self.le_arquivo(nome_arquivo)
    
    def busca(self, k, x=None):
        if x == None:
            return self.busca(k, self.raiz)
        else:
            i = 0
            while i < len(x.chaves) and k > x.chaves[i]:
                i += 1
            if i < len(x.chaves) and k == x.chaves[i]:
                return (x, i)
            elif x.folha:
                return None
            else:
                return self.busca(k, x.filhos[i])
            


B = arvoreB(2)
B.carrega_arquivo("0.tree")
i = int(input())
while(i != -1):
    if(B.busca(i) == None):
        print(str(i) + " nao encontrado")
    else:
        print(str(i) + " encontrado")
    i = int(input())