# Exercícios Python - Nível Intermediário

Este repositório contém três exercícios de Python focados em estruturas de controle como break, continue e uso do else com for (verificação de número primo).

# 1. Uso do break

Cria uma lista de números de 1 a 20 e para o loop ao encontrar o número 13.

# Código

for numero in range(1, 21):

  if numero == 13:

  break

Execução real:

![Execução break](https://github.com/Jefferson-Mattos/exercicios-python-intermediario/blob/main/imagens/break.png.png?raw=true)

#2. Uso do continue

Percorre a lista de 1 a 20 e imprime apenas os ímpares.

Código

for numero in range(1, 21):

  if numero % 2 == 0:

  continue

  print(numero)

Execução real:

![Execução continue](https://github.com/Jefferson-Mattos/exercicios-python-intermediario/blob/main/imagens/continue.png.png?raw=true)

#3. Verificação de número primo

Recebe um número e verifica se ele é primo utilizando else após o for.

Código

numero = int(input())

for i in range(2, numero):

  if numero % i == 0:

  break

else:

  print("É primo")

Execução real:

![Execução primo](https://github.com/Jefferson-Mattos/exercicios-python-intermediario/blob/main/imagens/primo.png.png?raw=true)

![Execução primo](https://github.com/Jefferson-Mattos/exercicios-python-intermediario/blob/main/imagens/primo1.png.png?raw=true)

Licença

MIT. Sinta-se livre para contribuir, melhorar ou usar os exemplos!