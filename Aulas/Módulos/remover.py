def remover_palavras(lista, blacklist):
    for palavra in blacklist:
        while palavra in lista:
            lista.remove(palavra)
    return lista