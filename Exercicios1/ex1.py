"""
## **Exercício 1: Limpeza e Substituição de Texto**

**Crie um programa que:**

**Receba uma frase do usuário. Remova os espaços em branco extras no início e no final da frase usando o método strip. Substitua todas as vírgulas (,) por pontos finais (.) usando o método replace. Exiba a frase modificada.**

- Receba uma **frase** do usuário.
- **Remova** os **espaços** em branco extras no início e no final da frase usando o método **strip**.
- **Substitua** todas as vírgulas (,) por pontos finais (.) usando o método **replace**.
- Exiba a frase modificada.
"""

fraseUser = input('Digite uma Frase: ')
print(fraseUser.replace(",", ".").strip())