"""
    Crie o Módulo contagem_palavras.py:

    - Defina uma função chamada contar_palavras que receba um texto como parâmetro.

    Implemente a Função contar_palavras:

    - Converter para Minúsculas: Use lower() para transformar todo o texto em minúsculas.
    - Dividir em Palavras: Utilize split() para separar o texto em uma lista de palavras.
    - Contar Palavras:
        - Inicialize um dicionário vazio para armazenar a contagem.
        - Percorra a lista de palavras e incremente a contagem de cada palavra no dicionário.
    - Retornar o Dicionário: Após a contagem, retorne o dicionário com as palavras e suas respectivas frequências.
"""

def contar_palavras(text):
    text = text.lower()
    words = text.split()
    word_count = {}
    i = 1
    for word in words:
        word_count[word] = i
        i += 1
    return word_count

text = "Dmitri é Feioso e Viado"

word_count = contar_palavras(text)
print(word_count)