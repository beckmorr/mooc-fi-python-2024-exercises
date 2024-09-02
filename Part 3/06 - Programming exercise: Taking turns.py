# Por favor, escreva um programa que peça ao usuário para digitar um número.
# O programa deve então imprimir os números inteiros positivos entre 1 e o número digitado,
# alternando entre as duas extremidades do intervalo, conforme nos exemplos abaixo.
#
# Exemplo de saída:
#
# Por favor, digite um número: 5
# 1
# 5
# 2
# 4
# 3
#
# Por favor, digite um número: 6
# 1
# 6
# 2
# 5
# 3
# 4
#
# Solução
number = int(input("Por favor, digite um número: "))
if number == 1:
    print(number)

index = 1

while index < number:
    print(index)
    print(number)
    index += 1
    number -= 1
    if index == number:
        print(index)
        
