"""
Função de Verificação de Número Primo

- Criar uma função que receba um número e retorne True se o número for primo, e False se não for.

Função Recursiva para Somar uma Lista

- Criar uma função recursiva que calcule a soma de todos os elementos de uma lista.

Função para Contagem de Palavras

- Escrever uma função que receba uma string e conte o número de palavras.

Função com *args e **kwargs para Registrar Várias Informações

- Criar uma função que aceite um número indeterminado de argumentos e informações extras nomeadas, e exiba-as.
"""

def é_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n % n == 0 and n > 1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return True

print(é_primo(17))
print(é_primo(15))

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])

print(soma_lista([1, 2, 3, 4, 5]))

def contar_palavras(texto):
    return len(texto.split())

print(contar_palavras("Olá, como vai você?"))

def registrar_informacoes(*args, **kwargs):
    print("Argumentos posicionais (*args):")
    for arg in args:
        print(arg)

    print("\nArgumentos nomeados (**kwargs):")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

registrar_informacoes(1, 2, 3, nome = "João", idade = 30, cidade = "São Paulo")