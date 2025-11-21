def saudacao(nome):
    return f"Olá, {nome}!"


def idade_para_100(idade):
    return 100 - idade


usuario = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(saudacao(usuario))
print(f"Faltam {idade_para_100(idade)} anos para você chegar aos 100 anos.")
