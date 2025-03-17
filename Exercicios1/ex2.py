"""
## **Exercício 2: Contagem de Palavras com Loop for**

**Crie um programa que:**

**Receba uma frase do usuário. Use o método split para separar a frase em palavras. Use um loop for para contar quantas palavras começam com a letra "a" (maiúscula ou minúscula). Exiba o número de palavras encontradas.**

- Receba uma **frase** do usuário.
- Use o método **split** para **separar** a frase em palavras.
- Use um **loop** for para **contar** quantas palavras **começam com** a letra "a" (maiúscula ou minúscula).
- Exiba o número de palavras encontradas.
"""
fraseUser = input('Digite uma Frase: ')
count = 0
countMin = 0
countMaiusc = 0
lista = fraseUser.split(" ")
print(fraseUser)
print(lista)
for item in lista:
    if item.startswith("a") == True:
        countMin += 1
        count += 1
    elif item.startswith("A") == True:
        countMaiusc += 1
        count += 1
if count == 0:
    print("Não existe nenhum A em sua frase!")
elif count >= 1:
    print(f"O numero de letras A são {count}. Sendo elas {countMin} minuscula(s) e {countMaiusc} maiuscula(s)!")
