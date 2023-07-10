#leitura do arquivo

f = open("arquivo.txt", "r")

for linha in f:
    print(linha.replace("/n", ""))

f.close