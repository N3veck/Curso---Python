from funcoes import cadastrar, listar, remover

itens = []

while True:
    print("\n[1] Cadastrar [2] Listar [3] Remover [0] Sair")
    op = input("Escolha: ").strip()

    if op == "1":
        nome = input("Item: ").strip()
        cadastrar(itens, nome)

    elif op == "2":
        listar(itens)

    elif op == "3":
        listar(itens)
        try:
            num = int(input("Digite o número do item para remover: "))
            remover(itens, num)
        except ValueError:
            print("⚠ Digite um número válido.")

    elif op == "0":
        break

    else:
        print("Opção inválida.")
