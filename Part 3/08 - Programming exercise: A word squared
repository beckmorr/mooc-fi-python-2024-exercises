# Escreva uma função chamada squared, que recebe uma string e um número inteiro como argumentos,
# e imprime um quadrado de caracteres conforme especificado pelos exemplos abaixo.
#
# Exemplo de uso:
#
# squared("ab", 3)
#
# Deve imprimir:
# aba
# bab
# aba
#
# squared("aybabtu", 5)
#
# Deve imprimir:
# aybab
# tuayb
# abtua
# ybabt
# uyaba

# Solução:
# Write your solution here
def squared(string, number):
    length = len(string)
    start_index = 0 

    for i in range(number):
        for j in range(number):
            print(string[(start_index + j) % length], end="")
        start_index += number
        print() 

if __name__ == '__main__':
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
