\# Exercícios Python - Nível Intermediário



Este repositório contém três exercícios de Python focados em estruturas de controle como `break`, `continue` e uso do `else` com `for` (verificação de número primo).



\# 1. Uso do break



Cria uma lista de números de 1 a 20 e para o loop ao encontrar o número 13.



\# Código



for numero in range(1, 21):

&nbsp;   if numero == 13:

&nbsp;       break



Execução real:



!\[Execução break](imagens/break.png.png)



\#2. Uso do continue



Percorre a lista de 1 a 20 e imprime apenas os ímpares.



Código



for numero in range(1, 21):

&nbsp;   if numero % 2 == 0:

&nbsp;       continue

&nbsp;   print(numero)



Execução real:



!\[Execução continue](imagens/continue.png.png)



\#3. Verificação de número primo

Recebe um número e verifica se ele é primo utilizando else após o for.



Código



numero = int(input())

for i in range(2, numero):

&nbsp;   if numero % i == 0:

&nbsp;       break

else:

&nbsp;   print("É primo")



Execução real:



!\[Execução primo](imagens/primo.png.png)

!\[Execução primo](imagens/primo1.png.png)



Licença



MIT. Sinta-se livre para contribuir, melhorar ou usar os exemplos!

