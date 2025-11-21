senha_correta = "python123"
tentativa = ""
tentativas = 0
max_tentativas = 3

while tentativa != senha_correta and tentativas < max_tentativas:
    tentativa = input("Digite a senha: ")
    tentativas += 1

    if tentativa == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print(f"Tentativa {tentativas} de {max_tentativas}")

if tentativa != senha_correta:
    print("Acesso bloqueado!")
