def cadastrar(lista, item):
    if item in lista:
        print("⚠ Item já existe na lista!")
    else:
        lista.append(item)
        print("✔ Item cadastrado!")


def listar(lista):
    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")


def remover(lista, numero):
    if numero < 1 or numero > len(lista):
        print("⚠ Número inválido.")
    else:
        removido = lista.pop(numero - 1)
        print(f"🗑 Item '{removido}' removido!")
