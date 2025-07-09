numero = int(input("Digite um número para verificar se é primo: "))

if numero < 2:
    print("Números menores que 2 não são primos.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo. Divisível por {i}.")
            break
    else:
        print(f"{numero} é primo.")
