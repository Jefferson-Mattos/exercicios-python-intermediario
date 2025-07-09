numeros = list(range(1, 21))

for numero in numeros:
    if numero == 13:
        print("Número 13 encontrado. Interrompendo o loop.")
        break
    print(numero)
