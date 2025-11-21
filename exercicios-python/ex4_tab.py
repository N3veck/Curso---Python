# Tabuada de um número escolhido
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# ----------------------------
# Tarefa extra: tabuadas de 1 a 10

print("\nTabuada de 1 a 10:\n")

for n in range(1, 11):
    print(f"\n--- Tabuada do {n} ---")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
