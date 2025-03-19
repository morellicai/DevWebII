"""
Descrição:

1. Passo 1: Crie uma lista com as notas de cinco alunos.
2. Passo 2: Use um loop foreach para calcular a soma das notas.
3. Passo 3: Crie uma função que recebe a soma das notas e o número de alunos, e retorna a média.
4. Passo 4: Exiba a média das notas na tela.
"""

notas = [8.5, 9.2, 7.8, 8.7, 9.5]
def media(nota):
    return soma / len(notas)

soma = 0
for nota in notas:
    soma += nota

media_notas = media(soma)

print(f"A média dos alunos é {media_notas}")