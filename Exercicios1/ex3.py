"""
 ## **Exercício 3:**

crie um programa para exibir uma lista de roupas e seus valores (lista fixa) * para facilitar pode ser duas listas

depois exiba uma opção de escolher o produto pelo número e ao produto escolhido salvar em outra lista (carrinho)

e perguntar se quer comprar mais, por fim exibir os produtos comprados
"""
listRoupa = {
    'Roupa1' : 100,
    'Roupa2' : 230,
    'Roupa3' : 120,
    'Roupa4' : 400
}
carrinho = []
total = 0
menu = """
=-=-Bem_vindo_à_Loja_de_Compras=-=
Temos um catalago de 4 roupas
[1] Roupa 1
[2] Roupa 2
[3] Roupa 3
[4] Roupa 4
[5] Sair
[6] Finalizar
--> """
while True:
        opcao = input(menu)
        if opcao.strip():
            opcao = int(opcao)
        else:
            print("Por favor, insira um número válido!")
            continue

        if opcao == 5:
            if carrinho == []:
                print("Obrigado por visitar nossa loja!")
                break
            elif carrinho:
                print("\n=== Resumo do carrinho ===")
                for item in carrinho:
                    print(f"- {item}: R${listRoupa[item]:.2f}")
                print(f"Total da compra: R${total:.2f}.")
                escolha = str(input("Deseja finalizar sua compra? [S/N]: ")).upper()
                if escolha == "S":
                    print("\n=== Finalizando compra ===")
                    print(f"Total: R${total:.2f}")
                    print("Obrigado por comprar!")
                    break
                else:
                    print("Obrigado por visitar nossa loja e volte sempre!")

        elif opcao == 6:
            if carrinho:
                print("\n=== Finalizando compra ===")
                print(f"Total: R${total:.2f}")
                print("Obrigado por comprar!")
            else:
                print("Seu carrinho está vazio!")
            break

        elif opcao == 1:
            print(f"O preço da roupa 1 é R${listRoupa['Roupa1']:.2f}")
            escolha = str(input("Deseja colocar no carrinho? [S/N]: ")).upper()
            if escolha == "S":
                carrinho.append('Roupa1')
                total += listRoupa['Roupa1']
                print("Roupa1 adicionada ao carrinho!")

        elif opcao == 2:
           print(f"O preço da roupa 2 é R${listRoupa['Roupa2']:.2f}")
           escolha = str(input("Deseja colocar no carrinho? [S/N]: ")).upper()
           if escolha == "S":
                carrinho.append('Roupa2')
                total += listRoupa['Roupa2']
                print("Roupa2 adicionada ao carrinho!")

        elif opcao == 3:
            print(f"O preço da roupa 3 é R${listRoupa['Roupa3']:.2f}")
            escolha = str(input("Deseja colocar no carrinho? [S/N]: ")).upper()
            if escolha == "S":
                carrinho.append('Roupa3')
                total += listRoupa['Roupa3']
                print("Roupa3 adicionada ao carrinho!")

        elif opcao == 4:
            print(f"O preço da roupa 4 é R${listRoupa['Roupa4']:.2f}")
            escolha = str(input("Deseja colocar no carrinho? [S/N]: ")).upper()
            if escolha == "S":
                carrinho.append('Roupa4')
                total += listRoupa['Roupa4']
                print("Roupa4 adicionada ao carrinho!")

        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 6.")
            if carrinho:
                print("\nSeu carrinho:")
                for item in carrinho:
                    print(f"- {item}: R${listRoupa[item]:.2f}")
                print(f"Total: R${total:.2f}\n")
