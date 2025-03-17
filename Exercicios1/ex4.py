"""
crie um programa que tenha um valor fixo que é seu dinheiro. ex. 1000, depois o programa irá pergunta, o nome do produto, o preço do produto, a quantidade do produto, e perguntar se quer adicionar mais itens.

no final deve exibir o novo saldo da carteira e o carrinho de compras

dica: 4 variáveis e lista = carrinho
"""
dinheiro = 1000
carrinho = []

while True:
    nomeProduto = input("Digite o nome do produto: ")
    precoProduto = float(input("Digite o preço do produto: "))
    quantidadeProduto = int(input("Quantos produtos?: "))

    total = precoProduto * quantidadeProduto

    if total > dinheiro:
        print("Saldo insuficiente! Você não pode adicionar este produto ao carrinho.")
    else:
        carrinho.append({
            "nome": nomeProduto,
            "preco": precoProduto,
            "quantidade": quantidadeProduto,
            "total": total
        })
        dinheiro -= total
        print(f"Produto adicionado ao carrinho! Saldo restante: R$ {dinheiro:.2f}")

    continuar = str(input("Deseja adicionar mais itens? [S/N]: ")).upper()
    if continuar != "S":
        break

print("\n=== Carrinho de Compras ===")
for item in carrinho:
    print(f"{item['quantidade']} x {item['nome']} - R$ {item['preco']:.2f} cada (Total: R$ {item['total']:.2f})")

print(f"\nSaldo final da carteira: R$ {dinheiro:.2f}")
