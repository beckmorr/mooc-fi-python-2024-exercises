# Por favor, escreva um programa que peça ao usuário para digitar um número.
# O programa deve então imprimir todos os valores inteiros positivos de 1 até o número digitado.
# No entanto, a ordem dos números é alterada para que cada par de números seja invertido.
# Ou seja, 2 vem antes de 1, 4 antes de 3 e assim por diante. Veja os exemplos abaixo para mais detalhes.
#
# Exemplo de saída:
#
# Por favor, digite um número: 5
# 2
# 1
# 4
# 3
# 5
#
# Por favor, digite um número: 6
# 2
# 1
# 4
# 3
# 6
# 5
#
# Solução:
number = int(input("Por favor, digite um número: "))
if number % 2 == 0:
    for i in range(1, number + 1, 2): # range(start, stop, step)
        print(i + 1)
        print(i)
else: # se o número for ímpar o último número será o próprio número digitado
    for i in range(1, number, 2):
        print(i + 1)
        print(i)
    print(number)

