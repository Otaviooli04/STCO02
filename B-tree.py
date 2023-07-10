# "que Deus perdoe essas pessoas ruins" - Didico, the Imperator

# no mínimo t filhos, no máximo 2t filhos
# no min t-1 chaves e no max 2t-1 chaves
# exceto árvore
# todo nó folha, está a mesma distância da raiz(perfeitamente balanceada)

class noh:
    def __init__(self):
        self.folha = True
        self.chaves = []
        self.filhos = []

class arvereB:
    def __init__(self, t):
        self.t = t
        self.raiz = noh()

    # a função quebra o filho i e sobe a mediana para o pai
    def dividir_filho(self, pai, i):
        t = self.t
        y = pai.filhos[i]
        z = noh()
        z.folha = y.folha
        pai.filhos.insert(i+1, z)
        pai.chaves.insert(i, y.chaves[t-1]) #mediana
        z.chaves = y.chaves[t:]
        y.chaves =y.chaves[:t-1]

        # se não for folha, cuidar dos filhos
        if y.folha == False:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t-1]


    def insere(self, dado):
        raiz = self.raiz
        num_chaves = len(raiz.chaves)
        if num_chaves == (2* self.t - 1):
            temp = noh()
            temp.folha = False
            temp.filhos.append(raiz)
            self.raiz = temp
            self.dividir_filho(temp, 0)
        self.insere_nao_cheio(raiz, dado,)

    def insere_nao_cheio (self, noh_atual, dado):
        i = len(noh_atual.chaves) - 1
        if noh_atual.folha:
            noh_atual.chaves.append((None, None))
            while i >= 0 and dado[0] < noh_atual.chaves[i][0]:
                noh_atual.chave[i+1] = noh_atual.chaves[i]
                i -= 1
            noh_atual.chaves[i+1] = dado
        else:
            while i >= 0 and dado[0] < noh_atual.chaves[i][0]:
                i -= 1
            i += 1
            if len(noh_atual.filho[i].chaves) == (2 * self.t) - 1:
                self.dividir_filho(x, i)
                if dado[0] > noh_atual.chaves[i][0]:
                    i += 1
            self.insere_nao_cheio(noh.filho[i], dado)


if __name__ == "__main__":
    B = arvereB(3)
    B.insere(1)